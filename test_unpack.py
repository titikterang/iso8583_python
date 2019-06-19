from iso_mods.dataElements import dataElements
from iso_mods.isoUnpacker import isoUnpacker

isomsg = "0210723A40010AE1800200180000000000025000041207031660747519014504120412601404501307274804495300RS000147        JAKARTA SELATANSETIA BUDI                              0490852 81446343000000025000000000300041003591452027360006133001"
unpacker = ISOUnpacker(isomsg)
deMap = DataElements()
unpacker.unpack()
