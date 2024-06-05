"""
   Oriol Barba Vázquez
   14/02/2023
   ASIXc M03 UF2 A1

   Descripció: LinuxCommands

"""
def diccionari():
    comandes = ("touch","grep","cat","fdisk","cmp","dmesg","man","top","htop","halt")
    parametresHelp = ("-h","--help")
    parametresVersion = ("-v","--version")
    return comandes, parametresHelp, parametresVersion
def versions():
    version = ["v0.5","v1.2","v1.4","v0.1","v1.3","v1.5","v1.7","v0.8","v0.6","v0.2"]
    return version
def ajuda():
    ajuda = ["The touch command is a standard command used in UNIX/Linux operating system which is used to create, change and modify timestamps of a file. ",
    "The grep filter searches a file for a particular pattern of characters, and displays all lines that contain that pattern.",
    "It can be used to display the content of a file, copy content from one file to another, concatenate the contents of multiple files, display the line number, display $ at the end of the line, etc.",
    "It is used for the view, create, delete, change, resize, copy and move partitions on a hard drive using the dialog-driven interface. ",
    "cmp command in Linux/UNIX is used to compare the two files byte by byte and helps you to find out whether the two files are identical or not.",
    "It used to control the kernel ring buffer. The output contains messages produced by the device drivers.",
    "man command in Linux is used to display the user manual of any command that we can run on the terminal. ",
    "top command is used to show the Linux processes. It provides a dynamic real-time view of the running system.",
    "htop command in Linux system is a command line utility that allows the user to interactively monitor the systems vital resources or servers processes in real time.",
    "The halt command writes data to the disk and then stops the processor. The machine does not restart. "]
    return ajuda
listaVersions = versions()
comandes,parametresHelp,parametresVersion = diccionari()
listaAjuda = ajuda()

while True:
    prompt = input("sjo@ahk-049-ha209-14:~$ ")
    if prompt == "halt":
        print("Apagant sistema")
        break
    if prompt == "":
        print("Cap comanda detectada")
        continue
    if len(prompt.split(" ")) == 2:
        comandaDividida = prompt.split(" ")
        comanda = comandaDividida[0]
        parametre = comandaDividida[1]
        if comanda in comandes and (parametre in parametresHelp or parametre in parametresVersion):
            if parametre in parametresVersion:
                posicioComanda = comandes.index(comanda)
                print(listaVersions[posicioComanda])

            elif parametre in parametresHelp:
                posicioComanda = comandes.index(comanda)
                print(listaAjuda[posicioComanda])
        else:
            print("Value <"+prompt+"> is not valid option BACALAO")
    else:
        print("Comanda no trobada")
