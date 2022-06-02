#!bin/bash
docker container inspect m_a > log.txt
docker container inspect m_b >> log.txt
docker container inspect m_c >> log.txt
docker container inspect r_a >> log.txt
docker container inspect r_b >> log.txt
docker container inspect r_c >> log.txt