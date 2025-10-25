# ROS2_Testings_pro3

Testing repository for ROS 2 bring-up on **Jetson (Ubuntu 22.04 / JetPack 6, ROS 2 Humble)** with:
- **CSI-Kamera** (libcamera/Argus oder V4L2, je nach JetPack)
- **LiDAR über UART** (z. B. LDS06C @ /dev/ttyTHS1)
- Entwicklung am **Host (Ubuntu 22.04)**, Deployment am **Jetson** via Git

> Quick start: Repo auf **Host** entwickeln → push → auf **Jetson** klonen → `rosdep install` → `colcon build` → `ros2 launch`.

---

## 0) Voraussetzungen

- **Host**: Ubuntu 22.04, ROS 2 **Humble**
- **Jetson**: Ubuntu 22.04 (JetPack 6.x), ROS 2 **Humble**
- Git, CMake/Build-Essentials
- Netzwerk (Host ↔ Jetson im gleichen Subnetz)

---

## 1) ROS 2 Humble installieren (Host **und** Jetson)

```bash
# Locale & Repo-Schlüssel
sudo apt update && sudo apt install -y locales curl gnupg lsb-release software-properties-common
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
sudo add-apt-repository universe -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | \
sudo tee /etc/apt/sources.list.d/ros2.list

sudo apt update
sudo apt install -y ros-humble-desktop \
  python3-colcon-common-extensions python3-rosdep build-essential cmake git

# rosdep initialisieren (einmalig pro Maschine)
sudo rosdep init || true
rosdep update

# Komfort (am Ende der ~/.bashrc auf beiden Systemen)
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
echo 'export ROS_DOMAIN_ID=7'           >> ~/.bashrc
echo 'export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp' >> ~/.bashrc
source ~/.bashrc


## Run demo bringup
```bash
ros2 launch ugv_bringup bringup_race.launch.py
# Toggle the leitsystem state from another terminal:
ros2 param set /leitsystem_interface ttl_yellow true   # -> 0.5 m/s limit
ros2 param set /leitsystem_interface ttl_green true    # -> green
ros2 param set /leitsystem_interface ttl_green false   # -> yellow if ttl_yellow true, else red
```

## Packages
- `ugv_msgs` – custom message definitions (Behavior, ParkingSlot(s))
- `ugv_v2x` – `/leitsys/state` + `/traffic_light/state` (fuser)
- `ugv_safety` – emergency brake (red) + collision monitor (LiDAR)
- `ugv_planning` – simple local planner stub (publishes `/cmd_vel`)
- `ugv_control` – speed limiter (green/yellow/red) + vehicle interface
- `ugv_bringup` – launch files and parameters
