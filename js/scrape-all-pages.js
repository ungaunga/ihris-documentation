const http = require('https');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const fs = require('fs');
const events = require('events');
const fd = new events.EventEmitter();
const host = 'https://wiki.ihris.org'; 
const Entities = require('html-entities').AllHtmlEntities

const images_url = 'https://wiki.ihris.org/wiki/File:Dhis_send.jpg'
const entity = new Entities();
const parent = require('path').resolve(__dirname, '..')
const index = fs.createWriteStream(`${parent}/index.rst`, {flags: `a+`});
const countries_idx = fs.createWriteStream(`${parent}/docs/countries/index.rst`, {flags: `a+`});
const countries = ['botswana', 'ghana', 'guatemala', 'india', 'kenya', 'lesotho', 
                    'malawi', 'mali', 'namibia', 'nigeria', 'rwanda', 'senegal',
                    'sierra_leone', 'tanzania', 'uganda']

fs.readFile(`${parent}/data/test.json`, 'utf-8', (err, data) => {
    if(err){
        console.log(err.message);
        return;
    };
    data = JSON.parse(data);
    data.forEach(category => {
        const text = category.text.split('(');
        if(!parseInt(text[1][0])) return;
        const title = category.url.substring(category.url.lastIndexOf(':')+1)
        let dir_name = title.toLowerCase().replace('_', '-')
        if(countries.includes(title.toLowerCase())){
            countries_idx.write(`\    ${dir_name}/index\n`);
            dir_name = `countries/${dir_name}`;
        } else {
            index.write(`\    docs/${dir_name}/index\n`);
        }
        fs.mkdir(`${parent}/docs/${dir_name}`, { recursive: true }, (err) =>  {
            if(err)
                console.log(err.message)
        });
        read_write_data(dir_name, category.url, text[0].trim());
    });
});

let read_write_data = function(dir, url, title){
    http.get(url, (res) => {
        let ndata = '';
        res.on('data', (chunk) => ndata += chunk);
        res.on('end', () => {
            let dom = new JSDOM(ndata).window.document;
            let pages = Array.from(dom.getElementById('mw-pages').getElementsByTagName('li'));
            let index_rst = fs.createWriteStream(`${parent}/docs/${dir}/index.rst`, {flags: 'a+'});
            index_rst.write(`${title}`)
            index_rst.write(`\n${title.replace(/./g, '=')}\n\n`); // make it title. same width underline
            index_rst.write(`.. toctree::\n\n`);
            index_rst.write(`\    :maxdepth: 2\n`);
            index_rst.write(`\    :caption: ${title}\n\n`);
            let count = 1;
            pages.forEach(page => { // for each page found
                if(!pages.length) return;
                let page_url = page.getElementsByTagName('a')[0].href;
                let page_edit_url = page_url.substring(page_url.lastIndexOf('/')+1);
                let page_title = page.getElementsByTagName('a')[0].innerHTML;
                let page_file_name = page_edit_url.toLowerCase().replace(/(\-{2,})|([()])/gi, '').replace(/(:)|(_-_)|(\.)|(_)+/gi, '-')
                index_rst.write(`\    ${page_file_name}\n`);
                let edit_url = `${host}/mediawiki/index.php?title=${page_edit_url}&action=edit`;
                console.log(edit_url)
                http.get(edit_url, (page_res) => {
                    let  content = '';
                    page_res.on('data', (chunks) => content += chunks);
                    page_res.on('end', () => {
                        let new_dom = new JSDOM(content).window.document;
                        let txt_area = new_dom.getElementById('wpTextbox1')
                        if(!txt_area) return;
                        txt_area = entity.decode(txt_area.innerHTML);
                        let ws = fs.createWriteStream(`${parent}/docs/${dir}/${page_file_name}.rst`, {flags: 'w+'});
                        ws.write(page_title);
                        ws.write(`\n${page_title.replace(/./g, '=')}\n\n`);
                        ws.write(txt_area);
                        ws.end(''); // must explicitly have this for close event to fire
                        ws.on('finish', () => fd.emit('close'));
                    });
                    count += 1;
                });
            });
            
        });
    }).on('error', (e) => {
        console.error(`Got an error: ${e.message}`);
    });
}