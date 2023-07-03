
import os
import subprocess

hashmap = {}

#command to download the successful build 

#copr-cli download-build 6057851

#have to get builder-live.log.gz from another folder called epel-7-x86_64

files = os.listdir()
cd = os.getcwd()

for file in files:
    
    count = 0
    if "fedora" in file:
        print(file)
        filepath = cd + "/" + file
        print(filepath)

        os.chdir(filepath)







        #command to unzip log file

        #gzip -d builder-live.log.gz

        unzipCommand = "gzip -d builder-live.log.gz"
        result = subprocess.run(unzipCommand, shell = True, capture_output = False, text = True)
        print(result.stdout)
        
        weirdFailures = []
        
        with open("builder-live.log", "r") as file:

            
            for line in file:
                
                if (count == 0):
                    if "test" in line and "FAILED" in line and "..." in line:

                        
                        hashmap[line] = 1
                else:
                    if "test" in line and "FAILED" in line and "..." in line:
                        
                        if (line not in hashmap):

                        
                            hashmap[line] = 1
                            name = line + file
                            weirdFailures.append(name)

                
                

        keys = list(hashmap.keys())
        
    
        print("----------------------------")
        for key in keys:
            print(key)
        
        count = count + 1

        print("Weird Failures")

        for failure in weirdFailures:
            print(failure)

