#Pythonda tanımlanmış değişkenleri varlığını kontrol etmek programın çökme (crush) hatalarının önlemesi açısından son derece önemlidir.
#Python'da, belirli bir değişkenin tanımlı olup olmadığını kontrol etmek için in anahtar kelimesini kullanabilirsiniz.

#Örneğin, aşağıdaki gibi bir kod bloğunda, degisken adlı bir değişken tanımlanır ve sonrasında if kontrol yapısı ile degiskenin tanımlı olup olmadığını kontrol edilir:

degisken = 42

if 'degisken' in locals():
    print("degisken tanimli!")
else:
    print("degisken tanimli degil!")

#Burada, locals() fonksiyonu yerel ad alanındaki tüm değişkenleri bir sözlük olarak döndürür.
#in anahtar kelimesi, locals() sözlüğünde degisken adlı bir anahtar varsa True değerini döndürür ve if bloğu çalıştırılır. 
#Aksi takdirde, else bloğu çalıştırılır.

#Benzer şekilde, bir modül içinde belirli bir değişkenin tanımlı olup olmadığını kontrol etmek için, hasattr() fonksiyonunu kullanabilirsiniz.
#Bu fonksiyon, bir nesnenin belirtilen bir özelliğe (attribute) sahip olup olmadığını kontrol eder.

#Örneğin, math modülünde pi sabiti tanımlıdır. Bu sabitin varlığını kontrol etmek için şu kodu kullanabilirsiniz:

import math

if hasattr(math, 'pi'):
 # math.pi fonksiyonu var!
    print("pi tanimli!")
else:
    print("pi tanimli degil!")

#burada, hasattr() fonksiyonu math modülünde pi adlı bir özelliğin (attribute) tanımlı olduğunu kontrol eder.
#pi tanımlı olduğu için if bloğu çalıştırılır ve ekrana "pi tanimli!" yazısı yazdırılır.
