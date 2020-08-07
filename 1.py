ipadress={"R1":"10.1.1.1",
          "R2":"10.0.0.2",
          "R3":"10.0.0.3",
          "S1":"10.0.0.4",
          "S2":"10.0.0.5"}

dict1={"usuario1":"123456789",
       "valor":5000,
       "edad":21,
       "casado":False,
       "Rate en %":52.2}
print(ipadress)
print(ipadress[0])
ipadress["S3"]="10.0.0.6"
print("S3" in ipadress)
print(5000 in dict1)
print("valor" in dict1)
print(dict1["usuario1"])