cd onos
sudo bazel run onos-local

% Una vez arrancado ONOS, ingresar a la GUI y activar las aplicaciones reactive forwarding (fwd) y openflow

cd ..
sudo mn --controller=remote --custom RedEspana.py --topo mytopo