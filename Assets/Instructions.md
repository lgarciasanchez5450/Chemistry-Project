Hello
In order to add more elements you follow the current convention of the other json files
1) The file name does not matter at all, feel free to name them however you want for organizational purposes
2) Each Element must have all tags filled out
3) The following link can help you fill out the  properties https://www.rsc.org/periodic-table/
4) A simple google search can help you fill out common uses & description
5) IMPORTANT if an element is a Lanthanide or Actinide, specify so in their "group" tag, otherwise just put a number
6) There are other tags like backgroundColor and such. You can use them to color code families like noble gases
7) Do not make Description too long, stick below 250 characters



Example for Element Hydrogen
{
    "backgroundColor":[100,100,150], 
    "textColor":[255,255,255],

    "group":1,
    "period":1,
    "symbol":"H",
    "family":"",
    "fullName":"Hydrogen",
    "AtomicNumber":1,
    "AtomicMass":1.008,
    "MeltingPointKelvin":13.99,
    "BoilingPointKelvin": 20.271,
    "CommonUses":"Common Uses: H Bombs",
    "Description":"This is the Description for Hydrogen"
}

Example for Element Lanthanum (Special Because of Lanthanide)
{
    "backgroundColor":[100,100,100], 
    "textColor":[255,255,255],

    "group":"Lanthanides",
    "period":6,
    "symbol":"La",
    "family":"Lanthanides",
    "fullName":"Lanthanum",
    "AtomicNumber":57,
    "AtomicMass":138.905,
    "MeltingPointKelvin":1193.0,
    "BoilingPointKelvin": 3737.0,
    "CommonUses":"Commonly used in many alloys to store hydrogen gas for vehicles. ",
    "Description":"Discovered by Carl Gustav Mosander in the year 1839. Lanthanum appears as a soft and silvery-white metal..."
}