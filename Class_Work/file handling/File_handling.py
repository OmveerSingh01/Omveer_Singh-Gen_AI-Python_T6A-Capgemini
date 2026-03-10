# here, total 3 different modes are present
#  1. write(w)
#  2. read(r)
#  3. append(a)

''' write mode
    1. only write(w),
    2. write + read(w+),
    3. write binary (wb),
    4. write and read binary(wb+)


    read mode
    1. only read(r),
    2. read + write(r+),
    3. read binary (rb),
    4. read and write binary(rb+)


     append mode
    1. only append(a),
    2. append + read (a+),
    3. append binary (ab),
    4. append and read binary(ab+)
'''

# for write operation ,
# 1. write(str_data) : Single line of data
# 2. writelines([line1,line2,.......,lineN]) : Multiple lines of dtata