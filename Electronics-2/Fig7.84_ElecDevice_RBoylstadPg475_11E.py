## Name: Avro Biswas
## Reg. No: 2020338038


# Import packages
import schemdraw
from schemdraw import elements as elm


with schemdraw.Drawing() as ckt:

    # Basic configuration of drawing environment
    ckt.config(unit=3)

    # Starting the drawing from left side with 14V supply
    ckt += elm.Dot(open=True).label('14 V')

    # The Resistor connected to the 14V supply
    ckt += elm.Resistor().right().length(4).label(r'$2.2\ k\Omega$')

    # The JFET(source connected to the Resistor)
    ckt += (jfet := elm.JFetP('down', circle=True, anchor='source', fill='#aaddff')
            .label(r'$V_P = -6\ V$',ofst=(-.2, 0), loc='right', color='#115577')
            .label(r'$I_{Dss} = 6\ mA$', ofst=(-0.6, 0), loc='right', color='#115577'))
    
    # The gate terminal of the JFET is grounded
    ckt += elm.Line().length(1.5).at(jfet.gate)
    ckt += elm.Ground()

    # Continue to add elements to the drain of the JFET
    ckt += elm.Line('right').length(1.5).at(jfet.drain)

    # Adding a node at the drain terminal
    ckt.push()

    # Output is connected to the node at drain terminal
    ckt += elm.Dot()
    ckt += elm.Line().length(1.5)
    ckt += elm.Dot(open=True).label(r'$V_S$', loc='right')

    # Going back to the node to add another branch
    ckt.pop()

    # Drain resistor and the ground
    ckt += elm.Resistor('down').length(2.4).label(r'$0.39\ k\Omega$', loc='bot')
    ckt.add(elm.Ground())

    ckt.save('Fig7.84_ElecDevice_RBoylstadPg475_11E.pdf')
    ckt.draw()