QReactor

Forked from qt5reactor which was forked from qt4reactor and now uses 
[qtpy](https://github.com/spyder-ide/qtpy) to provide to support both.

Using the QtReactor
-------------------

Install using pip

::

    pip install qt-reactor

Before running / importing any other Twisted code, invoke:

::

    app = QApplication(sys.argv) # your code to init QtCore
    from twisted.application import reactors
    reactors.installReactor('qt')

or

::

    app = QApplication(sys.argv) # your code to init QtCore
    import qreactor
    qreactor.install()

Testing
~~~~~~~

::

   trial --reactor=qt5 [twisted] [twisted.test] [twisted.test.test_internet]

Make sure the plugin directory is in path or in the current directory for
reactor discovery to work.

Testing on Python 3
~~~~~~~~~~~~~~~~~~~

``trial`` does not work on Python3 yet. Use Twisted's `Python 3 test runner`_ instead.

.. _Python 3 test runner: https://twistedmatrix.com/trac/browser/trunk/admin/run-python3-tests

Install the reactor before calling ``unittest.main()``.

::

    import qreactor
    qreactor.install()
    unittest.main(...)
