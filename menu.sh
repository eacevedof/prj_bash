#!/bin/sh

declare -a projects=("prj__docker" "prj__docker_ci" "prj__docker_imgs" "prj__doctrine2" "prj__elchalanaruba" "prj__flutter" "prj__js" "prj__jsonup" "prj__jswebpack" "prj__linux" "prj__mysqlhive" "prj__phptests" "prj__platziphp" "prj__python37" "prj__reactjs3" "prj__symfony" "prj__theframework" "prj__theframework_helpers" "prj__wordpress")

for i in "${projects[@]}"
do
    echo $i
done

for ((i=1;i<=$#;i++)); 
do

  if [ ${!i} = "-s" ] 
  then ((i++)) 
      var1=${!i};

  elif [ ${!i} = "-log" ];
  then ((i++)) 
      logFile=${!i};  

  elif [ ${!i} = "-x" ];
  then ((i++)) 
      var2=${!i};    

  elif [ ${!i} = "-p" ]; 
  then ((i++)) 
      var3=${!i};

  elif [ ${!i} = "-b" ];
  then ((i++)) 
      var4=${!i};

  elif [ ${!i} = "-l" ];
  then ((i++)) 
      var5=${!i}; 

  elif [ ${!i} = "-a" ];
  then ((i++)) 
      var6=${!i};
  fi

done;
