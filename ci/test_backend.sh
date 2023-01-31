#!/bin/bash
docker-compose -f docker/compose/test.yml run fala-q-eu-nao-te-escuto unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
