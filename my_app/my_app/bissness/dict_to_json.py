import json


def is_part_of(name: str, number: int) -> bool:
    try:
        index = name.index('-')
    except ValueError:
        index = len(name)
    return name[:index].find(str(number)) != -1


def vm_basic():
    global vm_json, vm, vm_number
    vm_json['vm_id'] = vm['vm_id' + str(vm_number)]
    del vm['vm_id' + str(vm_number)]
    vm_json['boxName'] = vm['boxName' + str(vm_number)]
    del vm['boxName' + str(vm_number)]
    vm_json['password'] = vm['password' + str(vm_number)]
    del vm['password' + str(vm_number)]


def vm_docker():
    global vm_json, vm, vm_number
    vm_json['dockerProvisioners'] = []
    docker_number = 1
    while 1:
        try:

            docker = {
                'imageName': vm['dockerImageName' + str(vm_number) + '-' + str(docker_number)],
                'containerName': vm['dockerContainerName' + str(vm_number) + '-' + str(docker_number)],
                'cmd': vm['dockerCommand' + str(vm_number) + '-' + str(docker_number)],
                'args': vm['dockerArgs' + str(vm_number) + '-' + str(docker_number)]
            }
            if {key: docker[key] for key in docker if docker[key]}:
                vm_json['dockerProvisioners'].append(docker)
            del vm['dockerImageName' + str(vm_number) + '-' + str(docker_number)]
            del vm['dockerContainerName' + str(vm_number) + '-' + str(docker_number)]
            del vm['dockerCommand' + str(vm_number) + '-' + str(docker_number)]
            del vm['dockerArgs' + str(vm_number) + '-' + str(docker_number)]
            docker_number += 1
        except KeyError:
            break


def vm_network():
    global vm_json, vm, vm_number
    vm_json['networks'] = []
    network_number = 1
    while 1:
        try:

            network = {
                'networkType': vm['networkType' + str(vm_number) + '-' + str(network_number)],
                'ipAssignment': vm['IpAssignment' + str(vm_number) + '-' + str(network_number)]
            }
            if network['ipAssignment'] == 'static':
                network['ipAddress'] = vm['ipAddress' + str(vm_number) + '-' + str(network_number)]

            if {key: network[key] for key in network if network[key]}:
                vm_json['networks'].append(network)
            del vm['networkType' + str(vm_number) + '-' + str(network_number)]
            del vm['IpAssignment' + str(vm_number) + '-' + str(network_number)]
            del vm['ipAddress' + str(vm_number) + '-' + str(network_number)]
            network_number += 1
        except KeyError:
            break


def vm_script():
    global vm_json, vm, vm_number
    vm_json['scriptProvisioners'] = []

    if vm['scriptProvisaioner' + str(vm_number)]:
        vm_json['scriptProvisioners'].append({"script": vm['scriptProvisaioner' + str(vm_number)]})


def vm_ansible():
    global vm_json, vm, vm_number
    vm_json['ansibleProvisioners'] = []

    if vm['ansibleProvisioning' + str(vm_number)]:
        vm_json['ansibleProvisioners'].append({"playbook": vm['ansibleProvisioning' + str(vm_number)]})


def dict_to_json(request: dict) -> str:
    global vm, vm_json, vm_number
    virtual_environment_json = {'virtualMachines': []}
    vm = {key: request[key] for key in request if is_part_of(key, 1)}
    vm_json = {}
    vm_number = 1
    while vm:
        # at this point we have each vm separately in a dict.
        # these methods will be applied on each vm separately
        vm_basic()
        vm_network()
        vm_docker()
        vm_script()
        vm_ansible()
        virtual_environment_json['vagrantEnvPath'] = request['vagrantEnvPath']
        virtual_environment_json['dockerImagesPaths'] = request['dockerImagesPaths']
        virtual_environment_json['vagrantBoxesPaths'] = request['vagrantBoxesPaths']

        virtual_environment_json['virtualMachines'].append(vm_json)
        # retrieve the next vm.
        vm_number += 1
        vm = {key: request[key] for key in request if is_part_of(key, vm_number)}
        vm_json = {}

    return json.dumps(virtual_environment_json, indent=2)


vm = {}
vm_json = {}
vm_number = 1
