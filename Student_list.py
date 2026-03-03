import pprint
student = [
{
        "nome": "Franco",
        "età": 65,
        "corso":     173,
},
{
        "nome": "Antonio",
        "età": 45,
        "corso":     11,
},
{
        "nome": "Carlo",
        "età": 11,
        "corso":     1000,
},
{
        "nome": "Teresa",
        "età": 12,
        "corso":     777,
}
]

def stampa_minorenni():
    minorenni = 0
    for studenti in student:
        #print(student)
        if studenti["età"] < 18:
            minorenni +=1
            
            print(f"{studenti["nome"]}")
    print(f"Gli studenti minorenni sono:", {minorenni})
    
stampa_minorenni()

def set_corsi(student):
    
    list=[]
    for studenti in student:
        list.append(studenti["corso"])
    set_list = len(list)
    print(f"{set_list}")
    
    lenght_list=len(list)
    lenght_set=len(set(list))
    
    total_duble = lenght_list - lenght_set
    
    if lenght_list > lenght_set:
        print(f" i duplicati sono: {total_duble}")
    else:
        print("non sono presenti duplicati")

set_corsi(student)