Today Topics

1- List

Def : 

2- Tuples

Def : tuples python ka build in method hai, sirf read only hota hai 1 bar define krne bad modify nh ho skta, example id card 1 bar banne k bad change nh ho skta

Syntax:

tuple_data = ()

Tuple me 2 built in method hote hain
1- count ()
tuple k andar us same name ki jinti bh values hongi unka count kr dega jese
c
id_card.count("Muhammad Sharoz")
ans = 1

2- index()
tuple k andar ye value jis index pr rkhi hongi us index ka batayega jese
id_card = ("Muhammad Sharoz","Muhammad Umar",24)
id_card.index(24)
ans = 2


2- Dictionary (Object)

Def : dictionary me multiple values store ki ja skti hain jese list me krte hain but difference ye hai k list me 1 hi tarah ka data store krte hain isme different tarah ka data store krne me confusion hai, isi lye hum dicionary use krte hain q k isme structural data store hota hai ye key value pair me hota hai, key lagana it's means kisi data pr label lagana jis se data pehchanne me asani hoti hai.

syntax :

order_food = {
    "key" : "value"
}

python me dictionary ko acces krne k lye square brackets ko use krte hain . notaion use nh krte.

print(order_food["order_id"])



Hints/Tips

1- jo index apki list me honge hum sirf usey hi use kr skte hain agr koi index exist nh krta or ap usey acces krna chahyn to error aayega
2- append list k end me elem ko add krta hai or insert 2 arguments leta hai 1st index or 2nd value
3- F string me f ka means hai format.
4- Dictionary me only square brackets se hi values ko acces kya jata hai or key ko quation me likha jata hai.



HomeWork 

1- list k last me ele ko add kryn