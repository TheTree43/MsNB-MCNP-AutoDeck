def card(deg):
    file=str(deg)+'\MsNB.inp'
    f = open(file, 'a')
    f.write('c      -----------\n')
    f.write('c      cell cards\n')
    f.write('c      -----------\n')
    f.write('100    1 -3.8     -10  22 -23         imp:n=1   $Core HALEU/FLiNaK Solution\n')
    f.write('c      ---\n')
    f.write('101    2 -7.92     10 -11  22 -23     imp:n=1   $Core Pipe 316SS\n')
    f.write('c      ---\n')
    f.write('102    4  -3.02    12 -13  26 -27     imp:n=1   $Shroud Liner BeO\n')
    f.write('c      ---\n')
    f.write('103    2  -7.92    13 -14  20 -21     imp:n=1   $Shroud 316SS\n')
    f.write('c      ---\n')
    f.write('200    2  -7.92   -13  27 -21         imp:n=1   $Shroud Lid 316SS\n')
    f.write('c      ---\n')
    f.write('201    4  -3.02   -12  23 -24         imp:n=1   $Reflector Cap BeO\n')
    f.write('c      ---\n')
    f.write('202    5  -2.52   -12  25 -22         imp:n=1   $Absorber Plug B4C\n')
    f.write('c      ---\n')
    f.write('203    2  -7.92   -13  20 -26         imp:n=1   $Shroud Tray 316SS\n')
    f.write('c      ---\n')
    f.write("300    4 -3.02     -30 22 -23         imp:n=1   $12 o'clock control drum\n")
    f.write('c      ---\n')
    f.write("301    5 -2.52     30 -31 22 -23 -32  imp:n=1   $12 o'clock absorber shield\n")
    f.write('c      ---\n')
    f.write("302    4 -3.02      30 -31 22 -23  32  imp:n=1  $12 o'clock reflector shield\n")
    f.write('c      ---\n')
    f.write("400    4 -3.02     -40 22 -23         imp:n=1    $2 o'clock control drum\n")
    f.write('c      ---\n')
    f.write("401    5 -2.52     40 -41 22 -23 -42  imp:n=1   $2 o'clock absorber shield\n")
    f.write('c      ---\n')
    f.write("402    4 -3.02     40 -41 22 -23  42  imp:n=1   $2 o'clock reflector shield\n")
    f.write('c      ---\n')
    f.write("500    4 -3.02    -50 22 -23         imp:n=1   $4 o'clock control drum\n")
    f.write('c      ---\n')
    f.write("501    5 -2.52     50 -51 22 -23 -52  imp:n=1   $4 o'clock absorber shield\n")
    f.write('c      ---\n')
    f.write("502    4 -3.02     50 -51 22 -23  52  imp:n=1   $4 o'clock reflector shield\n")
    f.write('c      ---\n')
    f.write("600    4 -3.02     -60 22 -23         imp:n=1    $6 o'clock control drum\n")
    f.write('c      ---\n')
    f.write("601    5 -2.52     60 -61 22 -23  -62  imp:n=1   $6 o'clock absorber shield\n")
    f.write('c      ---\n')
    f.write("602    4 -3.02      60 -61 22 -23  62  imp:n=1   $6 o'clock reflector shield\n")
    f.write('c      ---\n')
    f.write("700    4 -3.02    -70 22 -23         imp:n=1    $8 o'clock control drum\n")
    f.write('c      ---\n')
    f.write("701    5 -2.52     70 -71 22 -23 -72  imp:n=1   $8 o'clock absorber shield\n")
    f.write('c      ---\n')
    f.write("702    4 -3.02     70 -71 22 -23  72  imp:n=1   $8 o'clock reflector shield\n")
    f.write('c      ---\n')
    f.write("800    4 -3.02    -80 22 -23         imp:n=1   $10 o'clock control drum\n")
    f.write('c      ---\n')
    f.write("801    5 -2.52     80 -81 22 -23 -82  imp:n=1   $10 o'clock absorber shield\n")
    f.write('c      ---\n')
    f.write("802    4 -3.02     80 -81 22 -23  82  imp:n=1   $10 o'clock reflector shield\n")
    f.write('c      ---\n')
    f.write('900    3 -2.27  11 -12  22 -23\n')
    f.write('                   #300 #301 #302\n')
    f.write('                   #400 #401 #402\n')
    f.write('                   #500 #501 #502\n')
    f.write('                   #600 #601 #602\n')
    f.write('                   #700 #701 #702\n')
    f.write('                   #800 #801 #802    imp:n=1   $Annular Gap Graphite\n')
    f.write('c      ---\n')
    f.write('901    6 -0.00178 -12  24 -27         imp:n=1   $Top Buffer Argon\n')
    f.write('c      ---\n')
    f.write('902    6 -0.00178 -12 -25  26         imp:n=1   $Bottom Buffer Argon\n')
    f.write('c      ---\n')
    f.write('999    0           14:-20:21          imp:n=0   $void\n')
    f.write('c      -----------\n')
    f.write('c      end cell cards\n')
    f.write('c      -----------\n')
    f.close()
