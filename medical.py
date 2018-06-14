import xlrd as x
import time as m     
import matplotlib.pyplot as plt
import pygame
pygame.init()
l=[]
lprice=[]
def medicines(y,name,age):
    wb = x.open_workbook('medicin.xls')
    tabs = wb.sheet_by_index(0)
    syrups = wb.sheet_by_index(1)
    vaccines = wb.sheet_by_index(2)
    drips = wb.sheet_by_index(3)
    if y == 'cancer':
        cancer_tabs = tabs.col_values(0)
        tab_price = tabs.col_values(1)
        cancer_syrups = syrups.col_values(0)
        syrups_price = syrups.col_values(1)
        cancer_vaccines = vaccines.col_values(0)
        vaccines_price = vaccines.col_values(1)
        cancer_drips = drips.col_values(0)
        drips_price = drips.col_values(1)
        print('------------cancer----------------')
        print('tablt : ',' '.join(cancer_tabs[1:]))
        print('price : ',tab_price[1:])
        print('------------------------------------------')
        print('syrups : ',' '.join(cancer_syrups[1:]))
        print('price : ',syrups_price[1:])
        print('------------------------------------------')
        print('vaccines : ',' '.join(cancer_vaccines[1:]))
        print('price : ',vaccines_price[1:])
        print('------------------------------------------')
        print('drips : ',' '.join(cancer_drips[1:]))
        print('price : ',drips_price[1:])
        print('-------------------------------------------')
        print(' ')
        c=0
        d=0
        e=0
        f=0
        price =0
        m.sleep(2)
        while(c == 0):
            tablt = input('enter name of tablet :')
            if tablt in cancer_tabs:
                l.append(tablt)
                for z in range(1,len(cancer_tabs)):
                    if tablt == cancer_tabs[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * tab_price[z])
                        price  = price + (q * tab_price[z])
                        ask = input('yes if one more tab else no: ')
                        if ask == 'yes':
                            c=0
                        else:
                            print('price : ', price)
                            c=1
        print(' ')
        m.sleep(2)
        while(d == 0):
            tablt = input('enter name of syrup :')
            if tablt in cancer_syrups:
                l.append(tablt)
                for z in range(1,len(cancer_syrups)):
                    if tablt == cancer_syrups[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * syrups_price[z])
                        price  = price + (q * syrups_price[z])
                        ask = input('yes if one more syrup else no: ')
                        if ask == 'yes':
                            d=0
                        else:
                            print('price : ', price)
                            d=1
        print(' ')
        m.sleep(2)
        while(e == 0):
            tablt = input('enter name of vaccines :')
            if tablt in cancer_vaccines:
                l.append(tablt)
                for z in range(1,len(cancer_vaccines)):
                    if tablt == cancer_vaccines[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * vaccines_price[z])
                        price  = price + (q * vaccines_price[z])
                        ask = input('yes if one more vaccines else no: ')
                        if ask == 'yes':
                            e=0
                        else:
                            print('price : ', price)
                            e=1
        print(' ')
        m.sleep(2)
        while(f == 0):
            
            tablt = input('enter name of drips :')
            if tablt in cancer_drips:
                l.append(tablt)
                for z in range(1,len(cancer_drips)):
                    if tablt == cancer_drips[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * drips_price[z])
                        price  = price + (q * drips_price[z])
                        ask = input('yes if one more drips else no: ')
                        if ask == 'yes':
                            f=0
                        else:
                            l1=[]
                            l1price=[]
                            for i in l:
                                if i not in l1:
                                    l1.append(i)
                            for i in lprice:
                                if i not in l1price:
                                    l1price.append(i)

                            print('---------------------------------------------')
                            print('patient name: ',name)
                            print('patient age: ',age)
                            print('medicines : ',' '.join(l1))
                            print('---------------------------price : ', price)
                            left=[]
                            for i in range(2,2*len(l1)+1,2):
                                left.append(i)
                            height = l1price
                            tick_label = l1
                            plt.bar(left,height,tick_label = tick_label, width=0.8,color=['red', 'green'])
                            plt.xlabel('x-axis')
                            plt.ylabel('y-axis')
                            plt.title('medicines with prices')
                            plt.show()
                            drum = pygame.mixer.Sound('somethinjustlikethis.mp3')
                            drum.play()
                            f=1

        
        






    elif y == 'jaundice' :
        jaundice_tabs = tabs.col_values(2)
        tab_price = tabs.col_values(3)
        jaundice_syrups = syrups.col_values(2)
        syrups_price = syrups.col_values(3)
        jaundice_vaccines = vaccines.col_values(2)
        vaccines_price = vaccines.col_values(3)
        jaundice_drips = drips.col_values(2)
        drips_price = drips.col_values(3)
        print('------------jaundice-------------------')
        print('tablt : ',' '.join(jaundice_tabs[1:]))
        print('price : ',tab_price[1:])
        print('------------------------------------------')
        print('syrups : ',' '.join(jaundice_syrups[1:]))
        print('price : ',syrups_price[1:])
        print('------------------------------------------')
        print('vaccines : ',' '.join(jaundice_vaccines[1:]))
        print('price : ',vaccines_price[1:])
        print('------------------------------------------')
        print('drips : ',' '.join(jaundice_drips[1:]))
        print('price : ',drips_price[1:])
        print('-----------------------------------------')
        print(' ')

        c=0
        d=0
        e=0
        f=0
        price =0
        m.sleep(2)
        while(c == 0):
            tablt = input('enter name of tablet :')
            if tablt in jaundice_tabs:
                l.append(tablt)
                for z in range(1,len(jaundice_tabs)):
                    if tablt == jaundice_tabs[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * tab_price[z])
                        price  = price + (q * tab_price[z])
                        ask = input('yes if one more tab else no: ')
                        if ask == 'yes':
                            c=0
                        else:
                            print('price : ', price)
                            c=1
        print(' ')
        m.sleep(2)
        while(d == 0):
            tablt = input('enter name of syrup :')
            if tablt in jaundice_syrups:
                l.append(tablt)
                for z in range(1,len(jaundice_syrups)):
                    if tablt == jaundice_syrups[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * vaccines_price[z])
                        price  = price + (q * vaccines_price[z])
                        ask = input('yes if one more syrup else no: ')
                        if ask == 'yes':
                            d=0
                        else:
                            print('price : ', price)
                            d=1
        print(' ')
        m.sleep(2)
        while(e == 0):
            tablt = input('enter name of vaccines :')
            if tablt in jaundice_vaccines:
                l.append(tablt)
                for z in range(1,len(jaundice_vaccines)):
                    if tablt == jaundice_vaccines[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * vaccines_price[z])
                        price  = price + (q * vaccines_price[z])
                        ask = input('yes if one more vaccines else no: ')
                        if ask == 'yes':
                            e=0
                        else:
                            print('price : ', price)
                            e=1
        print(' ')
        m.sleep(2)
        while(f == 0):
            tablt = input('enter name of drips :')
            if tablt in jaundice_drips:
                l.append(tablt)
                for z in range(1,len(jaundice_drips)):
                    if tablt == jaundice_drips[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * drips_price[z])
                        price  = price + (q * drips_price[z])
                        ask = input('yes if one more drips else no: ')
                        if ask == 'yes':
                            f=0
                        else:
                            l1=[]
                            l1price=[]
                            for i in l:
                                if i not in l1:
                                    l1.append(i)
                            for i in lprice:
                                if i not in l1price:
                                    l1price.append(i)
                            print('------------------------------------------')
                            print('patient name: ',name)
                            print('patient age: ',age)
                            print('medicines : ',' '.join(l1))
                            print('--------------------------price : ', price)
                            left=[]
                            for i in range(2,2*len(l1)+1,2):
                                left.append(i)
                            height = l1price
                            tick_label = l1
                            plt.bar(left,height,tick_label = tick_label, width=0.8,color=['red', 'green'])
                            plt.xlabel('x-axis')
                            plt.ylabel('y-axis')
                            plt.title('medicines with prices')
                            plt.show()
                            drum = pygame.mixer.Sound('somethinjustlikethis.mp3')
                            drum.play()
                            f=1
        
                        

    elif y == 'cough':
        cough_tabs = tabs.col_values(4)
        tab_price = tabs.col_values(5)
        cough_syrups = syrups.col_values(4)
        syrups_price = syrups.col_values(5)
        cough_vaccines = vaccines.col_values(4)
        vaccines_price = vaccines.col_values(5)
        cough_drips = drips.col_values(4)
        drips_price = drips.col_values(5)
        print('---------------cough---------------')
        print('tablt : ',' '.join(cough_tabs[1:]))
        print('price : ',tab_price[1:])
        print('------------------------------------------')
        print('syrups : ',' '.join(cough_syrups[1:]))
        print('price : ',syrups_price[1:])
        print('------------------------------------------')
        print('vaccines : ',' '.join(cough_vaccines[1:]))
        print('price : ',vaccines_price[1:])
        print('------------------------------------------')
        print('drips : ',' '.join(cough_drips[1:]))
        print('price : ',drips_price[1:])

        c=0
        d=0
        e=0
        f=0
        price =0
        m.sleep(2)
        while(c == 0):
            tablt = input('enter name of tablet :')
            if tablt in cough_tabs:
                l.append(tablt)
                for z in range(1,len(cough_tabs)):
                    if tablt == cough_tabs[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * tab_price[z])
                        price  = price + (q * tab_price[z])
                        ask = input('yes if one more tab else no: ')
                        if ask == 'yes':
                            c=0
                        else:
                            print('price : ', price)
                            c=1
        print(' ')
        m.sleep(2)
        while(d == 0):
            tablt = input('enter name of syrup :')
            if tablt in cough_syrups:
                l.append(tablt)
                for z in range(1,len(cough_syrups)):
                    if tablt == cough_syrups[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * syrups_price[z])
                        price  = price + (q * syrups_price[z])
                        ask = input('yes if one more syrup else no: ')
                        if ask == 'yes':
                            d=0
                        else:
                            print('price : ', price)
                            d=1
        print(' ')
        m.sleep(2)
        while(e == 0):
            tablt = input('enter name of vaccines :')
            if tablt in cough_vaccines:
                l.append(tablt)
                for z in range(1,len(cough_vaccines)):
                    if tablt == cough_vaccines[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * vaccines_price[z])
                        price  = price + (q * vaccines_price[z])
                        ask = input('yes if one more vaccines else no: ')
                        if ask == 'yes':
                            e=0
                        else:
                            print('price : ', price)
                            e=1
        print(' ')
        m.sleep(2)
        while(f == 0):
            tablt = input('enter name of drips :')
            if tablt in cough_drips:
                l.append(tablt)
                for z in range(1,len(cough_drips)):
                    if tablt == cough_drips[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * drips_price[z])
                        price  = price + (q * drips_price[z])
                        ask = input('yes if one more drips else no: ')
                        if ask == 'yes':
                            f=0
                        else:
                            l1=[]
                            l1price=[]
                            for i in l:
                                if i not in l1:
                                    l1.append(i)
                            for i in lprice:
                                if i not in l1price:
                                    l1price.append(i)
                            print('---------------------------------------------')
                            print('patient name: ',name)
                            print('patient age: ',age)
                            print('medicines : ',' '.join(l1))
                            print('---------------------------price : ', price)
                            left=[]
                            for i in range(2,2*len(l1)+1,2):
                                left.append(i)
                            height = l1price
                            tick_label = l1
                            plt.bar(left,height,tick_label = tick_label, width=0.8,color=['red', 'green'])
                            plt.xlabel('x-axis')
                            plt.ylabel('y-axis')
                            plt.title('medicines with prices')
                            plt.show()
                            drum = pygame.mixer.Sound('somethinjustlikethis.mp3')
                            drum.play()
                            f=1
        

    elif y == 'skin':
        skin_tabs = tabs.col_values(6)
        tab_price = tabs.col_values(7)
        skin_syrups = syrups.col_values(6)
        syrups_price = syrups.col_values(7)
        skin_vaccines = vaccines.col_values(6)
        vaccines_price = vaccines.col_values(7)
        skin_drips = drips.col_values(6)
        drips_price = drips.col_values(7)
        print('--------------skin------------------------')
        print('tablt : ',' '.join(skin_tabs[1:]))
        print('price : ',tab_price[1:])
        print('------------------------------------------')
        print('syrups : ',' '.join(skin_syrups[1:]))
        print('price : ',syrups_price[1:])
        print('------------------------------------------')
        print('vaccines : ',' '.join(skin_vaccines[1:]))
        print('price : ',vaccines_price[1:])
        print('------------------------------------------')
        print('drips : ',' '.join(skin_drips[1:]))
        print('price : ',drips_price[1:])
        print('-------------------------------------------')
        print(' ')

        c=0
        d=0
        e=0
        f=0
        price =0
        m.sleep(2)
        while(c == 0):
            tablt = input('enter name of tablet :')
            if tablt in skin_tabs:
                l.append(tablt)
                for z in range(1,len(skin_tabs)):
                    if tablt == skin_tabs[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * tab_price[z])
                        price  = price + (q * tab_price[z])
                        ask = input('yes if one more tab else no: ')
                        if ask == 'yes':
                            c=0
                        else:
                            print('price : ', price)
                            c=1
        print(' ')
        m.sleep(2)
        while(d == 0):
            tablt = input('enter name of syrup :')
            if tablt in skin_syrups:
                l.append(tablt)
                for z in range(1,len(skin_syrups)):
                    if tablt == skin_syrups[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * syrups_price[z])
                        price  = price + (q * syrups_price[z])
                        ask = input('yes if one more syrup else no: ')
                        if ask == 'yes':
                            d=0
                        else:
                            print('price : ', price)
                            d=1
        print(' ')
        m.sleep(2)
        while(e == 0):
            tablt = input('enter name of vaccines :')
            if tablt in skin_vaccines:
                l.append(tablt)
                for z in range(1,len(skin_vaccines)):
                    if tablt == skin_vaccines[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * vaccines_price[z])
                        price  = price + (q * vaccines_price[z])
                        ask = input('yes if one more vaccines else no: ')
                        if ask == 'yes':
                            e=0
                        else:
                            print('price : ', price)
                            e=1
        print(' ')
        m.sleep(2)
        while(f == 0):
            tablt = input('enter name of drips :')
            if tablt in skin_drips:
                l.append(tablt)
                for z in range(1,len(skin_drips)):
                    if tablt == skin_drips[z]:
                        q = int(input('quantity : '))
                        lprice.append(q * drips_price[z])
                        price  = price + (q * drips_price[z])
                        ask = input('yes if one more drips else no: ')
                        if ask == 'yes':
                            f=0
                        else:
                            l1=[]
                            l1price=[]
                            for i in l:
                                if i not in l1:
                                    l1.append(i)
                            for i in lprice:
                                if i not in l1price:
                                    l1price.append(i)
                            print('-------------------------------------------')
                            print('patient name: ',name)
                            print('patient age: ',age)
                            print('medicines : ',' '.join(l1))
                            print('------------------------price : ', price)
                            left=[]
                            for i in range(2,2*len(l1)+1,2):
                                left.append(i)
                            height = l1price
                            tick_label = l1
                            plt.bar(left,height,tick_label = tick_label, width=0.8,color=['red', 'green'])
                            plt.xlabel('x-axis')
                            plt.ylabel('y-axis')
                            plt.title('medicines with prices')
                            plt.show()
                            drum = pygame.mixer.Sound('somethinjustlikethis.mp3')
                            drum.play()
                            f=1
    else:
        print('record not found')


def doctor_appointment():
    name = input('enter name of patient : ')
    age = input('enter age : ')
    s1 = input('enter symptom 1: ')
    s2 = input('enter symptom 2: ')
    s3 = input('enter symptom 3: ')
    wb = x.open_workbook('desease.xls')
    t=wb.sheet_by_index(0)
    cancer = t.row_values(0)
    m.sleep(2)
    jaundice = t.row_values(1)
    m.sleep(2)
    cough = t.row_values(2)
    m.sleep(2)
    skin = t.row_values(3)
    if s1 in cancer and s2 in cancer and s3 in cancer:
        medicines('cancer',name,age)
    if s1 in jaundice and s2 in jaundice and s3 in jaundice:
        medicines('jaundice',name,age)
    if s1 in cough and s2 in cough and s3 in cough:
        medicines('cough',name,age)
    if s1 in skin and s2 in skin and s3 in skin:
        medicines('skin',name,age)





print('hospital database')
print('-------------------------------------------')
print('enter your choice : ')
print('press 1 for doctor appointment')
print('press 2 for medical store visit')
m.sleep(2)
n = int(input('     '))
while(True):
    if(n == 1):
        doctor_appointment()
        break
    elif(n==2):
        name = input('enter patient name: ')
        age = input('enter patient age : ')
        a=input('enter disease name: ')
        medicines(a,name,age)
        break
    else:
        break
