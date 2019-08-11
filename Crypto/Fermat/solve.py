n = 8501573979070185143621162007527022281143718257909136603203536295758915620319098887148687554942144299992373612531893899946961022203960339775506252612576270030475443562455811282661544048647645147554863284974916737501478441145602833760679628565275514355032401824604742578288482767670840902834294204214603556573537852226235731174776004439516625345966475599631397612602490402792898305618369271895376289129638069410280286009447947518217379336365018743255758099446332399809204124333319605923108402804036221102268311278604271788541909675935921895706414791465184797816728792231710746471275753679199081253249119560406482211351678240988872800331321030741864325119186652898070291219269345655210169813662676862093149981993096143736353546529481526537376824379036457801930108685913868180884948346492328587518760136479731328577989586492130405686176873123521613173392692956593514423637363749018120946732167839181794836280615234905244519049460772863166501356166274014639945681966487043817134473155297652038710207583791084288701309888694457483318326946761104783870003717823755918066810868176245144218404273769894951869282718559755962583562782590290411905463328640310364136273590620892234722730315208976241357322265036037427146241047642315408185309879

from gmpy2 import iroot

def fermat(n):
    a = iroot(n,2)[0] + 1
    b2 = a*a - n
    while(not iroot(b2,2)[1]):
        a+=1
        b2 = a*a - n
    b=iroot(b2,2)[0]
    return (a-b,a+b)
print fermat(n)
