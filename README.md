# Forget Me Not – Smart Item Reminder System

## 📖 Overview
**Forget Me Not** is an embedded smart reminder system designed to prevent you from forgetting essential items (like your wallet, keys, or phone) when leaving your home. Using a **Raspberry Pi Pico**, magnetic door sensors, and a photoresistor-based tray detection system, the device raises an alarm if items remain on the tray when the door is opened.  

The system integrates a **screen and speaker alarm** to deliver both visual and audible notifications, ensuring users never leave without their essentials.

---

## ⚡ Features
- **Real-time item detection** using a photoresistor tray sensor.  
- **Magnetic door sensor** to trigger events when the door opens.  
- **Speaker & screen alerts** for immediate user feedback.  
- **Embedded design on Raspberry Pi Pico** for reliable, low-power operation.  

---

## 🛠️ Tech Stack & Components
- **Microcontroller**: Raspberry Pi Pico (C/C++ SDK)  
- **Sensors**:  
  - Magnetic door sensor (detects door open/close events)  
  - Photoresistor (detects presence of items on tray)  
- **Output Devices**:  
  - Speaker (audible alarm)  
  - Screen (visual notification)  
- **Programming**: C/C++ (Pico SDK), MicroPython (optional for prototyping)  
- **Design Focus**: Embedded systems, low-power optimization, human-centric IoT  

---

## 🔧 How It Works
1. Place your essential item (e.g., wallet) on the tray.  
2. When the door opens, the system checks tray status via the photoresistor.  
3. - If the item is still on the tray → **alarm triggers** (screen + speaker).  
   - If the tray is empty (item taken with you) → **no alarm**.  
4. PLL-based logic lowers clock frequency when idle, reducing power draw.  

---

## 🚀 Setup & Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/forget-me-not.git
   cd forget-me-not
