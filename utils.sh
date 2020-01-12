#!/bin/sh

# referencia https://linuxhint.com/return-string-bash-functions/
#file: utils.sh

get_so () 
{
  case "$(uname -s)" in
    Darwin)
      echo "ios"
      # return "ios"
      ;;

    Linux)
      echo "linux"
      # return "linux"
      ;;

    CYGWIN*|MINGW32*|MSYS*)
      echo "windows"
      # return "windows"
      ;;
    # Add here more strings to compare
    # See correspondence table at the bottom of this answer
    *)
      # return "unknown"
      echo "unknown"
      ;;
  esac
}

is_true ()
{
  if [ -z "$2" ]; then return 0; fi
  if [ -z "$1" ]; then return 0; fi

  # echo "is_true: 2: $2, 1:$1"
  if [ "$1" == "$2" ]; then return 0;  else return 1; fi
}

is_truestr()
{
  if is_true $1 $2; then echo "0"; else echo "1"; fi
}

is_win ()
{
  local strso=$(get_so)
  is_truestr $strso "windows"
  
}

is_ios ()
{
  local strso=$(get_so)
  is_truestr $strso "ios"
}

# is_true "xx" "yy"
# echo ${ is_true "aa" "jj" }

#value = $((is_true "xx" "xx"))

#echo $value
# get_so
#value=$(is_win)
# echo $value

# is_truestr "xx" "yy"

echo "win:" $(is_win)
echo "ios:" $(is_ios)
