import m5
from m5.objects import *
import sys

# 1. CREATE THE MOTHERBOARD (SYSTEM)
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]


# 2. CREATE THE CPU & BRANCH PREDICTOR (YOUR PROJECT CORE)
system.cpu = DerivO3CPU()

# Grab the predictor name from the command line arguments
# If no argument is given, it defaults to LocalBP
# Grab the predictor name from the command line arguments
predictor_type = sys.argv[1] if len(sys.argv) > 1 else "LocalBP"

if predictor_type == "LocalBP":
    system.cpu.branchPred.conditionalBranchPred = LocalBP()
elif predictor_type == "BiModeBP":
    system.cpu.branchPred.conditionalBranchPred = BiModeBP()
elif predictor_type == "TournamentBP":
    system.cpu.branchPred.conditionalBranchPred = TournamentBP()
elif predictor_type == "PerceptronBP":
    # The Machine Learning hardware predictor!
    system.cpu.branchPred.conditionalBranchPred = MultiperspectivePerceptron8KB()
else:
    print(f"Error: Unknown predictor {predictor_type}")
    sys.exit(1)

print(f"--- Configured CPU with {predictor_type} ---")

# 3. WIRE THE CPU TO MEMORY
system.membus = SystemXBar()

system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# 4. LOAD YOUR C PROGRAM
# It will now read the program name from the automation script!
binary_path = sys.argv[2] if len(sys.argv) > 2 else 's4_project_tests/branch_test_random'

system.workload = SEWorkload.init_compatible(binary_path)
process = Process()
process.cmd = [binary_path]
system.cpu.workload = process
system.cpu.createThreads()

# 5. RUN THE SIMULATION
root = Root(full_system=False, system=system)
m5.instantiate()

print("--- Starting the KTU S4 Project Simulation ---")
exit_event = m5.simulate()
print(f"--- Simulation Finished ---")
print(f"Reason for exit: {exit_event.getCause()}")
