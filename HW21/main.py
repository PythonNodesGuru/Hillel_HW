from adaptee import UkPlug
from adapter import UktoUsAdapter


my_plug = UkPlug()
my_plug.electricity_220v()
#220 Volt
my_plug = UktoUsAdapter()
my_plug.electricity_220v()
#110 Volt
