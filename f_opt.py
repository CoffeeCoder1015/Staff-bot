import sys
def opt_parser(header,args,function):
    optlst = sys.argv
    
    if header == "":
        header = " "

    if header in optlst or header == " ":

        if header == " " and len(optlst) == 1:
            optlst.extend(" ")

        if optlst[1] == header:
            exc = False

            try:
                del optlst[0]
                del optlst[0]
                
                for i in range(0,len(optlst)):
                    optlst[i] = "%s(\"%s\")"%(args[i],optlst[i])
                optlst=str(optlst).replace("[","").replace("]","").replace("'","")
                fwa = str("function(%s)"%(optlst))
                exec(fwa)
                exc = True
                
            except:
                if exc == False:
                    print("usage:")
                    print(f"\"file\" {header} {args}")
                    print(f"This functions only accepts {len(args)} arguments")
