import qreactor
qreactor.install()

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QPushButton

from twisted.internet.defer import inlineCallbacks, Deferred
from twisted.internet import reactor


def test_reactor_click(qtbot):
    widget = QPushButton()
    qtbot.addWidget(widget)
    
    # Register callback to record clicks
    clicks = []
    def on_clicked(e):
        clicks.append(e)
    widget.clicked.connect(on_clicked)
    
    def click():
        qtbot.mouseClick(widget, Qt.LeftButton)
    
    # Have twisted trigger a click
    reactor.callLater(0.1, click)
    qtbot.waitUntil(lambda: len(clicks) > 0)
    
