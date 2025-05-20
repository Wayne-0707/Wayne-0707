# Start

# Create Class for Computers
class Computer:
    def __init__(self):
        self.cpu = "Unknown"
        self.ram = "Unknown"
        self.storage = "Unknown"
        self.gpu = "Unknown"

    def specs(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, GPU: {self.gpu}"

class ComputerBuilder: # Create Class to build Computer
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer

    def reset_build(self):
        self.computer = Computer()  # Task: Properly resets the builder
        return self

# Demo Usage
builder = ComputerBuilder()
gaming_pc = builder.set_cpu("Intel i9").set_ram("32GB").set_storage("1TB SSD").set_gpu("RTX 4080").build()
print(gaming_pc.specs())

# Reset builder for a new build
builder.reset_build()
workstation_pc = builder.set_cpu("AMD Ryzen 9").set_ram("64GB").set_storage("2TB SSD").set_gpu("RTX 4090").build()
print(workstation_pc.specs())