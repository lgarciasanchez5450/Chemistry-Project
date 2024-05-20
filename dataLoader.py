from typing import Literal, Any
import json
import os
DATA_FOLDER = './Assets/'

ElementDataKey = Literal[
    "backgroundColor",
    "textColor",
    "group",
    "period",
    "symbol",
    "family",
    "fullName",
    "AtomicNumber",
    "AtomicMass",
    "MeltingPointKelvin",
    "BoilingPointKelvin",
    "CommonUses",
    "Description"
]

class ElementData(dict):
    def __getitem__(self, key: ElementDataKey) -> Any: 
        return super().__getitem__(key)
    def getBGColor(self) -> list[int]: return self['backgroundColor']
    def getTextColor(self) -> list[int]: return self['textColor']
    def group(self) -> int|str: return self['group']
    def period(self) -> int: return self['period']
    def symbol(self) -> str: return self['symbol']
    def family(self) -> str: return self['family']
    def fullName(self) -> str: return self['fullName']
    def atomicNumber(self) -> int: return self['AtomicNumber']
    def atomicMass(self) -> float: return self['AtomicMass']
    def meltingPointKelvin(self) -> float: return self['MeltingPointKelvin']
    def boilingPointKelvin(self) -> float: return self['BoilingPointKelvin']
    def commonUses(self) -> str: return self['CommonUses']
    def description(self) -> str: return self['Description']

def getAllElementsData() -> list[ElementData]:
    data = []
    for path,_dirs,files in os.walk(DATA_FOLDER):
        for file in files:
            if file.endswith('.json'):
               with open(path+"/"+file) as f:
                    try:
                        element = ElementData(json.load(f))
                    except:
                        print(file)
                    data.append(element)
    return data



