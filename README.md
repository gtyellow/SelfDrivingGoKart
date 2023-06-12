# SelfDrivingGoKart

This is incomplete at this time

WARNING:  This assumes some familiarity with stepper motors, arduino and electronics.  All of the electrical connections should be safe low voltage sigaling, but I can't guarantee that's the case especially if you get into the drive unit which you will not need to do.  No warranty for your safety or the safety of your equipment.  Use at your own risk.  

Using a laptop, arduino, a stepper motor and python as well as a ninebot gokart, create a self driving Go Kart. Please see the material readme with links to everything.  You will also need screw drivers, volt meter and jumper wires, as well as a way to secure a laptop.  I used a desk computer stand.  It might be possible to hold it in your lap, but it will be tight.  

I'm using a ninebot gokart pro from Segway for this build.  The segway has electric controls for the brake and throttle which 
connect well with the arduino.  To connect the arduino to the gokart, look on the underside of the gokart between the throttle and brake pedals.  There should be a small approximately two inch by three inch cover secured by two screws.  If you open that, you will see some wires with a connection socket.  The wider one with six connections is the controls for the brake and the throttle.  You can see where three wires go from to the brake and three go to the throttle.  You are going to want to bridge those with jumper wires, and measure the voltage when you apply the brake and throttle to each wire.  This will allow you to determine what is the positive, negative and ground for connecting to the arduino.  

