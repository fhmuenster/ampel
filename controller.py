import fischertechnik.factories as txtFactory
txtController = txtFactory.controller_factory.create_graphical_controller()
I1 = txtFactory.input_factory.create_push_button(txtController, 1)
O1 = txtFactory.output_factory.create_lamp(txtController, 1)
O2 = txtFactory.output_factory.create_lamp(txtController, 2)
