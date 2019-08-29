IHRIS Regional Rollout
======================

=Developing a Policy for iHRIS Manage Rollout=

Many countries are interested in decentralizing their HR management system.  Several of the countries where we work are currently rolling out their system. Namibia is rolling out their HR information management system to the regions; 3 regions are now connected and all 13 will be online by the end of 2010. In Tanzania, the country’s largest FBO, Christian Social Services Commission, is installing iHRIS Manage in its 5 zonal offices. Uganda is currently implementing their iHRIS Manage system in nine districts and plans to eventually roll the system out to all of the 83 districts. Expanding an information system requires careful planning and preparation and there are many details to consider. This article will highlight what we’ve learned thus far. As you read this article, please note the following: 

* Each country is governed differently and health care administration division varies greatly. Countries may be divided into zones, regions, districts, states, etc. For simplicity in this document, we will refer to all of these as regions.

* Each country also has a group of people making decisions about HRIS strengthening and software deployment. For simplicity in this document, we will refer to the decision makers as the ‘stakeholder leadership group’ or ‘SLG’ for short.

* Although this article is written for iHRIS Manage expansion, it may be applicable to other HR management systems as well.

Designating permission to Edit Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The iHRIS Manage data model for regional deployment requires the SLG to develop a policy designating whether data will be edited at the regional offices or at the central head office.  Data cannot be edited at both:

* A. Data edited at the regional offices are aggregated at the central office and are read-only at the central office.
* B. Data edited at the central office are sent to the regional offices and are read-only at the regional offices.

It is important to note that by choosing option B, a regional office will not be able to add a new employee, etc. to the list and will have to wait for the central office to do so.

Standardizing Lists
^^^^^^^^^^^^^^^^^^^

One advantage of data model B is it helps ensure consistency of database lists, which create dropdown menus, across the regional offices, which is crucial to aggregating data and producing meaningful reports. For example, if the SLG chooses to edit the list of cadres at the central office, a *Maternity Nurse*  in the Northern region, for instance, will be the same as a *Maternity Nurse*  in the Western and other regions.   If, on the other hand, the SLG chooses data model A and regional offices edit the cadre list, there would be no assurance that the *Maternity Nurse*  cadre in the Western region and Northern region are the same. In fact, there may be no *Maternity Nurse*  in the Northern region’s cadre list at all.  There may instead be a *Maternity and Infant Care Nurse*  in the Northern region.  These cadres may or may not be the same, and there would be no way for the software to know that. This can cause many problems when trying to produce and analyze reports on, say, how many ‘Maternity Nurses’ are employed nationally and in each district. Enforcing standardization of database lists is also important for job codes and job classifications. 

In general, if a database list contains choices which apply to more than one regional office, it would ideally be set to be edited at the central office and not at the regional office. Thus, as much as possible, the SLG should create standards for all of the dropdown lists which apply to more than one region. 

On the other hand, data/forms such as the personnel data, should be edited at the regional office. For instance, personnel data includes contact, demographic, and education information. This is because the regional offices will be more likely to have accurate data and to be involved in the day to day management of the personnel. Also, any lists that you will not likely be concerned about comparing data on at the central level should be safe to be edited at the regional level.

Step Solution
^^^^^^^^^^^^^

Although creating standardized lists for all drop-down lists is ideal, the SLG may not be able to do so before rollout begins. Based on zonal deployment in Tanzania, the iHRIS developers and stakeholders suggested the following lists to be edited at the zonal office:

* diocese
* position_type (full time, part time, temporary)
* department

As indicated in the example of cadres above, if you choose to edit a database list at the regional office rather than at the central office, it will make direct comparison of the data at the central office more difficult. However, you may have not had a chance to standardize all the lists with input from each of the regional offices. 

The **Step Solution**  is to allow the above lists (and a few others) to be edited at the regional offices.  Then, after some time has passed and the regional offices have each created their own lists of diocese, etc., the central office should review these lists and decide upon a standardized list that all the regional offices will use.  For example if the Northern region entered a department ‘Maternity Ward’ and the Western region entered a department ‘Maternity and Infant Ward,’ then the central office might decide that these are the same and choose to standardize it as "Maternity Ward."

Once a list has been standardized, each of the regional offices’ databases will need to be updated to use these lists, and to update any records pointing to "Maternity and Infant Ward" in the Western region now to "Maternity Ward" as defined by the head office. 

Using this sort of Step Solution will be a bit time consuming, so the more lists that can be defined and standardized before the regional deployment, the better.

