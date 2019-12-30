#!/bin/sh


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
