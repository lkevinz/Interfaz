from PyQt6.QtCore import QPropertyAnimation, QRect

def animate_button(button):
    """Expande el botón cuando el cursor entra."""
    anim = QPropertyAnimation(button, b"geometry")
    anim.setDuration(100)
    anim.setStartValue(button.geometry())
    anim.setEndValue(QRect(button.x()-5, button.y()-5, button.width()+10, button.height()+10))
    
    # Guardar la animación dentro del botón para evitar que se destruya
    button.animEnter = anim
    return anim

def reset_button(button):
    """Restaura el tamaño del botón cuando el cursor sale."""
    anim = QPropertyAnimation(button, b"geometry")
    anim.setDuration(100)
    anim.setStartValue(QRect(button.x()-5, button.y()-5, button.width()+10, button.height()+10))
    anim.setEndValue(button.geometry())

    # Guardar la animación dentro del botón para evitar que se destruya
    button.animLeave = anim
    return anim
