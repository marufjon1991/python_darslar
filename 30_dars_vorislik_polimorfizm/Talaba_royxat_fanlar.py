#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:59:31 2021

@author: dudu
"""

class Talaba:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya
        self.fanlar = []
    
    def fanga_yozil(self, fan_nomi):
        self.fanlar.append(fan_nomi)
        return self.fanlar
    
    def remove_fan(self, fan_nomi):
        if fan_nomi in self.fanlar:
            self.fanlar.remove(fan_nomi)
        else:
            print("Siz bu fanga yozilmagansiz")
        
class Fan:
    def __init__(self, fan_nomi):
        self.fan_nomi = fan_nomi
    
    def get_info(self):
        return self.fan_nomi
    
        
fan_1 = Fan('matematika')
fan_2 = Fan('Tarix')
talaba_1 = Talaba('Valijon', 'Bozorov')

talaba_1.fanga_yozil(fan_1.get_info())
talaba_1.fanga_yozil(fan_2.get_info())
print(talaba_1.fanlar)

talaba_1.remove_fan("matematika")
print(talaba_1.fanlar)

#Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, 
#Sotuvchi, Mijoz va hokazo)

#Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
#Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
#Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini 
#yarating.
#Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi
# bloklandi" degan matn chiqarsin.

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil):
        super().__init__(ism, familiya, passport, tyil)






























