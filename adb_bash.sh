# function find_midpoint {
#     echo $1
#     echo $2
#     if [[ $1 =~ $2 ]]
#     then
#         x1 = ${BASH_REMATCH[0]}
#         y1 = ${BASH_REMATCH[1]}
#         x2 = ${BASH_REMATCH[2]}
#         y2 = ${BASH_REMATCH[3]}
#         midpointx=($x1+$x2)/2
#         midpointy=($x1+$x2)/2
#         echo "$midpointx $midpointy"
#     else
#         echo "$1 doesn't match $2" >&2
#     fi 
# }

# TODO: avoid hardcoding these 

function save_xml {
    ./adb.exe shell uiautomator dump | awk '{gsub("UI hierchary dumped to: /sdcard/window_dump.xml", "");print}' 
    sleep 3
    echo `./adb.exe pull /sdcard/window_dump.xml`
    # python get-bounds.py  $1 $2
}

function start_app { 
    ./adb.exe shell monkey -p com.tuya.smartlife -c android.intent.category.LAUNCHER 1
    sleep 10
}

function reach_invite {
    # Me
    ./adb.exe shell input touchscreen tap "600 1294"

    # Home Management
    sleep 5
    ./adb.exe shell input touchscreen tap "372 776"

    # Join a home
    ./adb.exe shell input touchscreen tap 360.0 512.0

    # Invitation code
    ./adb.exe shell input touchscreen tap 360.0 510.0
}

function dump_to_console {
    ./adb.exe exec-out uiautomator dump /dev/tty | awk '{gsub("UI hierchary dumped to: /dev/tty", "");print}'
}

function leave_home { 
    ./adb shell input touchscreen swipe 500 1000 300 300
    ./adb shell input touchscreen swipe 500 1000 300 300
    ./adb shell input touchscreen swipe 500 1000 300 300
    ./adb shell input touchscreen swipe 500 1000 300 300
    sleep 1
    ./adb.exe shell input touchscreen tap 360.0 1256.0
    sleep 1 
    ./adb.exe shell input touchscreen tap 360.0 1158.0
}

# AT EACH NEW SCREEN 
# to find out where to tap, print out the xml layout to the tty 
# then pretty print it online
# then copy that output into an XML file 
# then determine the corresponding fields of interest (usually 'text' and 'whatever text field you want')
# then run `python get-bounds.py <your xml file> <tag> <field>` to get the x and y midpoints (tap coordinates)
# then run `./adb.exe shell input touchscreen tap x_here y_here`

start_app 
reach_invite

# try brute forcer (incomplete)
# python adb_mt_combos.py 6 

# type in new password 
# ./adb.exe shell input keyboard text "EK7UPW"

# # # perform screen tap (resource-id: com.tuya.smartlife:id/iv_invite_confirm)
# ./adb.exe shell input touchscreen tap 573.0 510.0
# sleep 1

# # on fail tap Got It.
# ./adb.exe shell input touchscreen tap 360.0 788.0;

# # leave home if needed
# leave_home

# USE xpath if available. Not available on Windows! 
# coords=$(perl 'printf "%d %d\n", ($1+$3)/2, ($2+$4)/2 if /content\-desc="me\_more"[^>]*bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"/' $xml)
# echo $coords
# regex=".*content-desc=\"me_more\".*bounds=\"\[(\d+),(\d+)\]\[(\d+),(\d+)\]\".*"
# bounds1=$(midpoint $xml $regex)
# echo $bounds1
# ./adb shell input touchscreen tap $bounds1