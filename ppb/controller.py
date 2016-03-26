import ppb.engine as engine
from ppb.event import Tick


class Controller(object):
    """
    A basic controller interface.

    Requires a hardware middleware that provides access to a keys, mouse, and
    events function.
    """

    def __init__(self, scene, hardware):
        """
        Attributes: keys: A dictionary of the hardware keys
                    mouse: An object definition of a mouse

        :param scene: Publisher
        :param hardware: An object with a keys, mouse and events functions.
                         keys should return a dictionary of the key state.
                         mouse should return an object representation of the mouse.
                         events should return hardware events translated into ppb events.
        :return:
        """
        scene.subscribe(Tick, id(self), self.tick)
        self.keys = None
        self.mouse = None
        self.hardware = hardware

    def tick(self, event):
        """
        Update the key and mouse state. Push hardware events to the queue.

        :param event: ppb.Event
        :return:
        """

        self.keys = self.hardware.keys()
        self.mouse = self.hardware.mouse()
        events = self.hardware.events()
        for e in events:
            engine.message(e)