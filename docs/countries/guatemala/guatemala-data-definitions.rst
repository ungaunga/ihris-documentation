Guatemala Data Definitions
==========================

This is the way Guatemala Data is organized.

<code>
[17:29:33] Sovello Hildebrand Mgani: hello Ricardo, i think we need a new branch on Launchpad for Guatemala

[17:32:57] Ricardo López Rodas: Yes, I think will be a good idea

[17:33:19] Sovello Hildebrand Mgani: so that in it we name everything Guatemala

[17:33:29] Ricardo López Rodas: If you do that, I can update my server with Bazar?

[17:34:06] Sovello Hildebrand Mgani: yes. that should then be by tomorrow morning when you come to office. you'll also see some of the lists ready!

[17:34:28] Ricardo López Rodas: GREAT!!

[17:38:11] Ricardo López Rodas: We can use iHRIS Guatemala for project in laouchpad

[17:38:44] Sovello Hildebrand Mgani: ok. i think you can go ahead and set the project. then i'll push code to it later

[17:38:58] Ricardo López Rodas: ok I will create today

[17:39:09] Sovello Hildebrand Mgani: then just send the details to me

[17:40:36] Ricardo López Rodas: Ok

[18:08:29] Sovello Hildebrand Mgani: sorry, will you have time. i got some questions to ask

[18:08:52] Ricardo López Rodas: Yes, tell me

[18:09:28] Sovello Hildebrand Mgani: ok. the Regiones, Departamentos, Municipios e Establecimientos, how are then related hierarchically

[18:09:40] Sovello Hildebrand Mgani: are the Regiones geographical?

[18:10:02] Ricardo López Rodas: Yes

[18:10:23] Ricardo López Rodas: Regiones content Departamentos

[18:10:41] Ricardo López Rodas: and Departamentos content Municipios

[18:10:52] Sovello Hildebrand Mgani: i hope you have used iHRIS before, haven't you?

[18:11:51] Ricardo López Rodas: Well, I can setup but for development I don't have experiencie

[18:12:19] Ricardo López Rodas: I Complete de course but I thinks this structure its more complex

[18:12:40] Sovello Hildebrand Mgani: ok.

[18:12:46] Sovello Hildebrand Mgani: ok. so regions have departments

[18:12:58] Sovello Hildebrand Mgani: and departments are not geographical.

[18:13:31] Sovello Hildebrand Mgani: departments contain municipalities, right? are municipalities direct under regions in geographical hierachy or something else?

[18:14:54] Sovello Hildebrand Mgani: or, to put it simple, just fill in the template file i sent you and try your best that I get it today, so that tomorrow morning when i get into office i work on some stuff and then will have something to demo by tomorrow morning (your day)

[18:15:33] Sovello Hildebrand Mgani: establishments are like facilities, right?

[18:16:04] Ricardo López Rodas: Regons, Departaments and Municipios are grographical hierachy

[18:16:28] Sovello Hildebrand Mgani: oooh!

[18:16:34] Ricardo López Rodas: Yes, establecimientos are Facilieties

[18:16:54] Sovello Hildebrand Mgani: i was thinking departments here are like departments in a school or an office or organization

[18:17:19] Sovello Hildebrand Mgani: and the UnidadEjecutora (executive units)?

[18:17:44] Ricardo López Rodas: Unidad Ejecutora it's a Budget division

[18:18:03] Sovello Hildebrand Mgani: ok. so a facility belongs to Unidad Ejecutora

[18:18:22] Ricardo López Rodas: also belongs to the Unidad Ejecutora

[18:18:24] Ricardo López Rodas: yes

[18:19:15] Sovello Hildebrand Mgani: and the Unidad Ejecutora are specialized into specializations (Areas) and types (Tipo Unidad)

[18:20:28] Ricardo López Rodas: it's like a division

[18:20:31] Ricardo López Rodas: for example

[18:20:49] Ricardo López Rodas: the area it's Health Area

[18:21:03] Ricardo López Rodas: in the first level

[18:21:49] Ricardo López Rodas: and for TIPO UNIDAD its type of Unidad Ejecutora Like Hospitals

[18:22:37] Ricardo López Rodas: Here In Guatmala the National a Regional Hospitals have a Especfic Budget that why have a Unidad ejecutora

[18:22:56] Sovello Hildebrand Mgani: in UnidadEjecutora table i find UnidadEjecutora e NomUEjecutora. how are they different?

[18:23:51] Ricardo López Rodas: yes, the Unidad Ejecutora it's the official CODE

[18:24:02] Ricardo López Rodas: and NomEjecutora it's tjhe NAME

[18:24:29] Sovello Hildebrand Mgani: oooh!

[18:24:57] Sovello Hildebrand Mgani: so the UnidadEjecutora here is predefined.

[18:25:11] Ricardo López Rodas: yes

[18:25:44] Sovello Hildebrand Mgani: And ClaseAncha?

[18:26:31] Ricardo López Rodas: ok, this is very special code

[18:27:00] Ricardo López Rodas: For employees in the MOH have diferent bugets codes

[18:27:14] Ricardo López Rodas: for example the REGLON

[18:27:39] Ricardo López Rodas: and are official codes too

[18:28:03] Ricardo López Rodas: for example the REGLON 11 are for permanent employees

[18:28:50] Ricardo López Rodas: the 22 it's for employees under contract that needs create a new contract each year

[18:29:12] Sovello Hildebrand Mgani: ok.

[18:29:40] Ricardo López Rodas: and CLASE ANCHA its a division of post especif for reglon 11

[18:30:30] Sovello Hildebrand Mgani: but there is no direct relationship (hierarchy) between Reglones Presupuestarios and ClaseAncha

[18:30:56] Ricardo López Rodas: it's correct

[18:31:03] Sovello Hildebrand Mgani: ok.

[18:31:49] Sovello Hildebrand Mgani: so if i were to group these. i would put Reglones Presupuestarios, ClaseAncha, TipoUnidad, Areas e UnidadEjecutora under Budget Lists say!

[18:33:00] Sovello Hildebrand Mgani: and would put Regiones, Departamentos e Municpios under Geographical Lists

[18:33:15] Ricardo López Rodas: I thinks it's correct

[18:33:55] Ricardo López Rodas: But I have a issue, the MOH technicians tell me that theay are generating a new pool of data

[18:33:56] Sovello Hildebrand Mgani: and put Establecimientos e TipoServicio under Facility Lists

[18:34:18] Ricardo López Rodas: with the same structure but for January 2013

[18:34:27] Sovello Hildebrand Mgani: ok.

[18:35:01] Sovello Hildebrand Mgani: what is in ServicioPersonal?

[18:35:33] Sovello Hildebrand Mgani: Especialidades goes into Qualifications list and Puo

[18:35:36] Ricardo López Rodas: Establecimientos it's Facily

[18:35:58] Sovello Hildebrand Mgani: and POSTS (Puestos) under Position lists

[18:36:13] Ricardo López Rodas: yes

[18:36:23] Sovello Hildebrand Mgani: how do you describe ServicioPersonal then?

[18:37:31] Ricardo López Rodas: Servicio Personal it's a big division, only have a 5 records and groups all Doctors, Nurseries,

[18:38:31] Sovello Hildebrand Mgani: ok. so we have to say for example this Sovello belongs to Doctors Servicio Personal, right?

[18:38:42] Ricardo López Rodas: They want to create reports for acumulate persos in these divisions

[18:38:49] Ricardo López Rodas: yes

[18:38:58] Sovello Hildebrand Mgani: ok. that's perfect. Now in the Personas Table

[18:39:41] Sovello Hildebrand Mgani: Why do we have again here CodEstablecimiento, CodUEjecutora, CodDepto, CodRegion?

[18:41:18] Sovello Hildebrand Mgani: which are already linked to Establecimientos? or is it possible to appear that the facility (Establecimiento) one is working is under one UnidadEjecutora and an employee at that same Establecimiento belongs to a different UnidadEjecutora?

[18:42:46] Ricardo López Rodas: give a second

[18:45:51] Ricardo López Rodas: In the table of Personas I put the UnidadEjecutora because some persons only assign to a UnidadEjecutora and We don't know at wich facily belongs

[18:47:00] Ricardo López Rodas: for that reason employees have NO ASIGNADO en Establecimientos

[18:48:10] Ricardo López Rodas: when the database will working we will do a data update

[18:48:31] Sovello Hildebrand Mgani: ok

[18:49:06] Ricardo López Rodas: Unidad Ejecutra in Personas will be temporaly field

[18:50:28] Sovello Hildebrand Mgani: ok

[18:50:50] Sovello Hildebrand Mgani: and CodDept here is it like the Domicile?

[18:53:17] Ricardo López Rodas: no, it's the same issue of Unidad Ejecutora, if the employee it's assign to a facility it's not necesary this filed

[18:53:42] Ricardo López Rodas: for domicile only have a final address

[18:53:52] Ricardo López Rodas: it's the field DIRECCION

[18:54:30] Ricardo López Rodas: part of the data update will be put the correct departamento and municipio for the address

[18:54:56] Sovello Hildebrand Mgani: ok.

[18:56:38] Sovello Hildebrand Mgani: should we maintain the three first names (nombre1..3) and surnames apellido1..2 or we can group say like firstname, surname and othernames?

[18:58:23] Ricardo López Rodas: The MOH wants to separete names and here in Guatemala have persons with 3 names

[18:59:51] Ricardo López Rodas: Surnames are commonly two per person

[18:59:55] Sovello Hildebrand Mgani: ok

[19:00:26] Ricardo López Rodas: but for the womans add the 3th surename when married

[19:01:28] Ricardo López Rodas: that it's apellidocasada or MarriedLastName

[19:02:26] Ricardo López Rodas: when can we have a blackboard for training

[19:02:58] Sovello Hildebrand Mgani: training about this?

[19:03:15] Ricardo López Rodas: yes

[19:03:18] Ricardo López Rodas: if its possible

[19:03:37] Sovello Hildebrand Mgani: well, we can always arrange!

[19:03:42] Sovello Hildebrand Mgani: what about friday?

[19:04:06] Ricardo López Rodas: it's ok for you

[19:04:09] Sovello Hildebrand Mgani: or thursday evening?

[19:04:34] Sovello Hildebrand Mgani: let's schedule for thursday! 18:00hrs EAT

[19:04:58] Ricardo López Rodas: ok perfect, my time?

[19:05:15] Ricardo López Rodas: I will create the Elluminate

[19:05:23] Sovello Hildebrand Mgani: what time is it now?

[19:05:33] Ricardo López Rodas: here is 10:00 am

[19:06:00] Sovello Hildebrand Mgani: ok. so it should be 09:00 am for you and 18:00 for me

[19:06:07] Ricardo López Rodas: perfect

[19:06:10] Ricardo López Rodas: thanks

[19:06:46] Ricardo López Rodas: I will create the webinar

[19:06:57] Ricardo López Rodas: I will send you the code

[19:12:10] Sovello Hildebrand Mgani: ok!

</code>
Cheers

[[Category:Guatemala]]
