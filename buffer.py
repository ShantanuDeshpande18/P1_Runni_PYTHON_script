import arcpy

arcpy.env.workspace = r"D:\MSC\sem_3\ProgGIS#3\Prac1_Running_Python\P1_Runni_PYTHON_script\Practical_1_ProProject\01_Running_Python_Scripts.gdb"

#performing buffer operation

arcpy.analysis.Buffer("Wilson_Schools", "Wilson_Schools_Buffer_2", "500 meters")

print("Proceess done")