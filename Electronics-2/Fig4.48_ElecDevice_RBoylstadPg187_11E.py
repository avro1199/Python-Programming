# This python script will produce a BET network
#Common-collecter(emitter-follower) configuration
# Fig.4.48
#Example 4.16
# Page:187
# Book: Electronic Devices and Circuit Theory
# By Robert L. Boylestad, Louis Nashelsky
# 11th Edition
#Registration no :2019338082

#Import the necessary packages
# Using the python package "SchemDraw"
# For more about the SchemDraw package please visit
# Project Link: https://schemdraw.readthedocs.io/en/latest/index.html

# The greek leter is produced with Unicode

#import necessery moduels
import schemdraw
import schemdraw.elements as elm
with schemdraw.Drawing() as d:
    d.config(unit=3)
    #npn transistor
    npn=elm.BjtNpn(circle=True,fill='skyblue').label(('-','$V_{CE_Q}$','+'),color='skyblue').label(r'$\beta\ =\ 90$',ofst=(.8,0),color='skyblue')
    d+=npn
    #collector terminal elements
    d+=elm.Ground().left()
    #base terminal elements
    d+=elm.Line().left().at(npn.base).length(2)
    d+=elm.Dot()
    d.push()
    
    d+=elm.Resistor().down().length(2).label('$R_B$').label(r'$\ 240\ k \Omega$',loc='bottom') ##Base terminal resistance of R_B=240kΩ
    d+=elm.Ground()
    d.pop()
    
    d+=elm.Capacitor2().left().length(3).label('$10 \mu F$', loc='bottom').label('$C_1$',loc='top')  ##Base terminal capacitance of C_1=10µF
    d+=elm.Dot(open=True).label('$v_i$')  ##input terminal voltage vi
    #emitter terminal elements
    d+=elm.Line().at(npn.emitter).down().length(.75)
    d+=elm.Dot()
    d.push()
    
    d+=elm.Capacitor2().right().length(2).label('$10 \mu F$',loc='bottom').label('$C_2$',loc='top') ##Emitter terminal capacitance of C_2=10µF
    
    d+=elm.Dot(open=True).label('$v_o$') ##output terminal voltage vo
    d.pop()
    d += elm.Resistor('down').length(2).label('$R_E$', loc='top').label('2 kΩ',loc='bot').label('$I_{E_Q}$',loc='bot',fontsize=15,ofst=(.4,.15),color='deepskyblue')  ##emitter terminal resistance of R_E=2kΩ    
    d += elm.Dot(open=True).down().label('$V_{EE}$',loc='top').label('-20 V',loc='bot')  ##Emitter terminal dc voltage V_EE= -20V
    d.save('Fig4.48_ElecDevice_RBoylstadPg187_11E.pdf')  ##pdf of schematic drawing
    d.draw()

