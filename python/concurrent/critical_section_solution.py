#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020 Gabriele Iannetti <g.iannetti@gsi.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Filename: critical_section_solution.py
#


import logging
import multiprocessing
import random
import time


class CriticalSection:

    def __init__(self, lock, block=True, timeout=None):

        self._lock = lock
        self._block = block
        self._timeout = timeout
        self._lock_acquired = False

    def __enter__(self):

        self._lock_acquired = self._lock.acquire(self._block, self._timeout)
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if self._lock_acquired:

            self._lock.release()
            self._lock_acquired = False

    def is_locked(self):
        return self._lock_acquired


def worker_func(wid, lock):

    logging.info("Started Worker: %s" % wid)

    with CriticalSection(lock, timeout=1.5) as critical_section:

        logging.info("Lock acquired: %s", critical_section.is_locked())

        if critical_section.is_locked():

            logging.info("Worker[%s] - locked" % wid)

            work_time = random.randint(0, 3)
            logging.info("Work time: %s" % work_time)
            time.sleep(work_time)

            logging.info("Worker[%s] - released" % wid)

    return


# You should see the following error message, if it comes to a race condition
# between process p1 and p2 (the probability is 50% per program run):
#
# ---> ValueError: semaphore or lock released too many times

def main():

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

    logging.info("START")

    mp_lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=worker_func, args=(1, mp_lock,))
    p2 = multiprocessing.Process(target=worker_func, args=(2, mp_lock,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    logging.info("END")


if __name__ == '__main__':
    main()

