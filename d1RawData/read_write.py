#===============================================================================
# @author: Norbert
# @date: 02/02/2019
#===============================================================================

# Heading(Columns) are separated by tab
header_cols = "FarmID\t" + "Address\t" + "StreetNum\t" + "StreetName\t" + \
            "SufType\t" + "Dir\t" + "City\t" + "Province\t" + "PostalCode\t"
rawd_cols_split, rawd_first_col, strname_addr_list, strname_list = [], [], [], []
body, street, suftype, province, postal_code, str_number = '', '', '', '', '', ''
dirname, rd_col2, faddr, str_suftype, pdir = '', '', '', '', ''

with open("d1RawListOfFarmsPHAGAS.txt", "r") as ifile, \
    open("d1ResultListOfFarmsPHAGAS.txt", "w") as ofile:
    # skip the raw data header...
    next(ifile)
    # write the new headers to the file first...
    ofile.write(header_cols)
    
    for line in ifile:
        rawd_cols_split = line.split('\t')
        rawd_first_col = rawd_cols_split[0]
        
        rd_col2 = rawd_cols_split[1][:-1]
        strname_addr_list = rd_col2.split(',')
        strname_list = strname_addr_list[0].split(' ')
        faddr = ', '.join(strname_addr_list)
        str_number = strname_list[0]
        
        str_suftype = strname_list[1:]
        pdir = str_suftype[-1]
        province = str(strname_addr_list[2]).strip()[:2]
        postal_code = str(strname_addr_list[2]).strip()[2:]
        
        if pdir.lower() in ["s", "n", "e", "w"]:
            streetlist = str_suftype[:-2]
            street = ' '.join(streetlist)
            suftype = str_suftype[-2]
            dirname = str_suftype[-1]
        else:
            streetlist = str_suftype[:-1]
            street = ' '.join(streetlist)
            suftype = str_suftype[-1]
            dirname = ''
                
        # ouput body...
        body = rawd_first_col + '\t' + faddr + '\t' + str_number \
               + '\t' + street + '\t'+ suftype + '\t'+ dirname \
               + '\t'+ strname_addr_list[1] \
               + '\t'+ province \
               + '\t'+ postal_code+'\n'
               
        # finally: write to file...
        ofile.write(body)
        
# done...
print (20*'*')
print ('success!!!')
print (20*'*')



