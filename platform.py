# Building a SoC in python with Migen
# http://brandonhamilton.github.io/building-a-soc-with-migen

from mibuild.generic_platform import *
from mibuild.xilinx_ise import XilinxISEPlatform, CRG_DS

_io = [
    # System clock (Differential 200MHz)
    ("clk200", 0,
        Subsignal("p", Pins("J9"), IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")),
        Subsignal("n", Pins("H9"), IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE"))
    ),

    # User clock (66MHz)
    ("clk66", 0, Pins("U23"), IOStandard("LVCMOS25")),

    # CPU reset switch
    ("cpu_reset", 0, Pins("H10"), IOStandard("SSTL15")),

    # USB-to-UART
    ("serial", 0,
        Subsignal("tx", Pins("J25"), IOStandard("LVCMOS25")),
        Subsignal("rx", Pins("J24"), IOStandard("LVCMOS25"))
    ),

    # LEDs
    ("user_led", 0, Pins("AC22"), IOStandard("LVCMOS25"), Misc("SLEW=SLOW")),
    ("user_led", 1, Pins("AC24"), IOStandard("LVCMOS25"), Misc("SLEW=SLOW")),
    ("user_led", 2, Pins("AE22"), IOStandard("LVCMOS25"), Misc("SLEW=SLOW")),
    ("user_led", 3, Pins("AE23"), IOStandard("LVCMOS25"), Misc("SLEW=SLOW")),
    ("user_led", 4, Pins("AB23"), IOStandard("LVCMOS25"), Misc("SLEW=SLOW")),
    ("user_led", 5, Pins("AG23"), IOStandard("LVCMOS25"), Misc("SLEW=SLOW")),
    ("user_led", 6, Pins("AE24"), IOStandard("LVCMOS25"), Misc("SLEW=SLOW")),
    ("user_led", 7, Pins("AD24"), IOStandard("LVCMOS25"), Misc("SLEW=SLOW")),
]

class Platform(XilinxISEPlatform):
    def __init__(self):
        XilinxISEPlatform.__init__(self, "xc6vlx240t-ff1156-1", _io,
            lambda p: CRG_DS(p, "clk200", "cpu_reset", 5.0))