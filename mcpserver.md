# Minecraft Server Setup and Management Guide

![Minecraft Server](https://www.minecraft.net/content/dam/games/minecraft/key-art/MC_2019Card.jpg)

## Introduction

This guide is designed to help GDG WOW Pune community members set up and manage their own Minecraft servers. Minecraft servers can be an excellent way to practice system administration, networking, and collaborative coding skills. They also provide a fun platform for community building and engagement.

## Prerequisites

Before setting up a Minecraft server, ensure you have:

- A computer with at least 4GB RAM (8GB recommended)
- Stable internet connection with a minimum upload speed of 5 Mbps
- Java Development Kit (JDK) 17 or newer
- Basic understanding of command line interfaces
- Familiarity with port forwarding on your router (if hosting from home)

## Server Types

### 1. Vanilla Server

The official Minecraft server software provided by Mojang. Simple to set up but offers limited customization.

### 2. Paper Server

An optimized fork of Spigot that offers better performance and more features.

### 3. Fabric Server

A lightweight, modular modding toolchain for Minecraft, focused on flexibility and ease of use.

### 4. Forge Server

The most popular modding platform that allows for extensive modification of the game.

## Basic Setup Instructions

### Step 1: Install Java

```bash
# For Ubuntu/Debian
sudo apt update
sudo apt install openjdk-17-jdk

# For CentOS/RHEL
sudo yum install java-17-openjdk-devel

# For Windows
# Download and install from Oracle's website
```

### Step 2: Download Server Software

```bash
# Create a directory for your server
mkdir minecraft-server
cd minecraft-server

# Download the server jar (Paper example)
wget https://papermc.io/api/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar -O paper.jar
```

### Step 3: Create a Startup Script

#### For Linux (start.sh):
```bash
#!/bin/bash
java -Xms2G -Xmx4G -jar paper.jar nogui
```

#### For Windows (start.bat):
```batch
@echo off
java -Xms2G -Xmx4G -jar paper.jar nogui
pause
```

Make the script executable (Linux):
```bash
chmod +x start.sh
```

### Step 4: Run the Server for the First Time

```bash
# Linux
./start.sh

# Windows
start.bat
```

Accept the EULA by editing the eula.txt file and changing `eula=false` to `eula=true`.

### Step 5: Configure the Server

Edit the `server.properties` file to configure your server:

```properties
server-port=25565
gamemode=survival
difficulty=normal
max-players=20
view-distance=10
spawn-protection=16
pvp=true
```

## Advanced Server Management

### Using Docker

Docker makes it easy to deploy and manage your Minecraft server in a containerized environment.

```bash
# Pull the Minecraft server image
docker pull itzg/minecraft-server

# Run the server
docker run -d -p 25565:25565 -e EULA=TRUE -e TYPE=PAPER -e VERSION=1.19.4 --name mc-server itzg/minecraft-server
```

### Setting Up Automated Backups

Create a backup script (Linux):

```bash
#!/bin/bash
DATE=$(date +%Y-%m-%d_%H-%M)
BACKUP_DIR="/path/to/backups"
SERVER_DIR="/path/to/minecraft-server"

# Stop the server
screen -S minecraft -X stuff "say Server is backing up in 10 seconds...^M"
sleep 10
screen -S minecraft -X stuff "save-all^M"
sleep 5
screen -S minecraft -X stuff "save-off^M"
sleep 2

# Create backup
tar -czf "$BACKUP_DIR/backup-$DATE.tar.gz" -C "$SERVER_DIR" .

# Resume the server
screen -S minecraft -X stuff "save-on^M"
screen -S minecraft -X stuff "say Backup complete!^M"

# Delete backups older than 7 days
find "$BACKUP_DIR" -name "backup-*.tar.gz" -mtime +7 -delete
```

### Setting Up a Minecraft Server on Cloud

#### AWS EC2 Setup

1. Launch an EC2 instance (t3.medium or better)
2. Configure security groups to allow port 25565
3. Connect via SSH and follow the basic setup instructions
4. Consider using an Elastic IP for a persistent address

#### Google Cloud Setup

1. Create a Compute Engine VM instance
2. Allow TCP port 25565 in firewall rules
3. Install and configure the server as above

## Server Performance Optimization

### Java Flags for Better Performance

```bash
java -Xms4G -Xmx4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -jar paper.jar nogui
```

### Optimizing server.properties

```properties
view-distance=8
simulation-distance=6
entity-activation-range-animals=16
entity-activation-range-monsters=24
entity-activation-range-villagers=16
max-entity-cramming=24
```

## Plugins and Mods

### Essential Plugins for Paper/Spigot

1. **EssentialsX** - Core commands and features
2. **WorldEdit** - In-game world editing
3. **CoreProtect** - Rollback and anti-grief
4. **LuckPerms** - Permission management
5. **Multiverse-Core** - Multiple world management

### Popular Mods for Fabric/Forge

1. **Lithium** - Performance improvements
2. **Starlight** - Light engine optimization
3. **Create** - Automation and machinery
4. **Terralith** - World generation enhancement
5. **Just Enough Items (JEI)** - Item management

## Community Engagement Ideas

1. **Collaborative Build Projects** - Assign themed build challenges
2. **Programming Competitions** - Develop plugins or mods for specific challenges
3. **Technical Workshops** - How to create custom plugins/mods
4. **Server Administration Training** - Teach server management skills
5. **Infrastructure Analysis** - Study server performance and optimization

## Contributing to this Guide

If you have improvements or additions to this guide, please submit a pull request or open an issue on our GitHub repository.

## Resources

- [Official Minecraft Server Download](https://www.minecraft.net/en-us/download/server)
- [Paper MC](https://papermc.io/)
- [Fabric](https://fabricmc.net/)
- [Forge](https://files.minecraftforge.net/)
- [Minecraft Wiki](https://minecraft.fandom.com/wiki/Minecraft_Wiki)

---

© 2025 GDG WOW Pune | This is not an official Google product