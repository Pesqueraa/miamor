class Persona:
    def __init__(self, nombre, año_nacimiento, genero, nacionalidad, profesion, estado_civil, altura, peso):
        """
        Constructor de la clase Persona
        __init__ se ejecuta automáticamente al crear una instancia
        """
        # Atributos requeridos
        self.nombre = nombre
        self.año_nacimiento = año_nacimiento
        
        # 4 atributos adicionales de mi invención
        self.genero = genero
        self.nacionalidad = nacionalidad
        self.profesion = profesion
        self.estado_civil = estado_civil
        
        # Más atributos adicionales
        self.altura = altura  # en metros
        self.peso = peso      # en kilogramos
        self.hobbies = []     # lista de hobbies
        self.activo = True    # estado activo/inactivo
    
    def saludar(self):
        """Método requerido que saluda con nombre y edad"""
        edad = self.calcular_edad()
        print(f"Hola, me llamo {self.nombre} y tengo {edad} años")
    
    def calcular_edad(self):
        """Método adicional 1: Calcula la edad actual"""
        from datetime import datetime
        año_actual = datetime.now().year
        return año_actual - self.año_nacimiento
    
    def calcular_imc(self):
        """Método adicional 2: Calcula el Índice de Masa Corporal"""
        if self.altura > 0:
            imc = self.peso / (self.altura ** 2)
            return round(imc, 2)
        return 0
    
    def agregar_hobby(self, hobby):
        """Método adicional 3: Agrega un hobby a la lista"""
        self.hobbies.append(hobby)
        print(f"✅ {self.nombre} ahora practica: {hobby}")
    
    def mostrar_info_completa(self):
        """Método adicional 4: Muestra información completa"""
        print(f"\n{'='*50}")
        print(f"INFORMACIÓN COMPLETA DE {self.nombre.upper()}")
        print(f"{'='*50}")
        print(f"📝 Nombre: {self.nombre}")
        print(f"🎂 Año de nacimiento: {self.año_nacimiento}")
        print(f"🔢 Edad: {self.calcular_edad()} años")
        print(f"⚧️ Género: {self.genero}")
        print(f"🌍 Nacionalidad: {self.nacionalidad}")
        print(f"💼 Profesión: {self.profesion}")
        print(f"💍 Estado civil: {self.estado_civil}")
        print(f"📏 Altura: {self.altura} m")
        print(f"⚖️ Peso: {self.peso} kg")
        print(f"🏥 IMC: {self.calcular_imc()}")
        print(f"🎯 Hobbies: {', '.join(self.hobbies) if self.hobbies else 'Ninguno'}")
        print(f"🟢 Activo: {'Sí' if self.activo else 'No'}")
    
    def cambiar_profesion(self, nueva_profesion):
        """Método adicional 5: Cambia la profesión"""
        profesion_anterior = self.profesion
        self.profesion = nueva_profesion
        print(f"🔄 {self.nombre} cambió de profesión: {profesion_anterior} → {nueva_profesion}")
    
    def es_mayor_de_edad(self):
        """Método adicional 6: Verifica si es mayor de edad"""
        return self.calcular_edad() >= 18
    
    def __str__(self):
        """
        Método especial para representación en string
        Se ejecuta al usar print(objeto) o str(objeto)
        """
        edad = self.calcular_edad()
        return f"👤 {self.nombre} ({edad} años) - {self.profesion} - {self.nacionalidad}"

# Ejemplo de uso y demostración
if __name__ == "__main__":
    print("CREANDO PERSONAS...")
    print("=" * 60)
    
    # Crear primera persona
    persona1 = Persona(
        nombre="María González",
        año_nacimiento=1995,
        genero="Femenino",
        nacionalidad="Mexicana",
        profesion="Ingeniera de Software",
        estado_civil="Soltera",
        altura=1.65,
        peso=58
    )
    
    # Usar los métodos de persona1
    print("Persona 1 creada:")
    persona1.saludar()  # Método requerido
    
    # Agregar hobbies
    persona1.agregar_hobby("Programar")
    persona1.agregar_hobby("Leer")
    persona1.agregar_hobby("Yoga")
    
    # Mostrar información completa
    persona1.mostrar_info_completa()
    
    # Probar otros métodos
    print(f"\n¿Es mayor de edad? {persona1.es_mayor_de_edad()}")
    persona1.cambiar_profesion("Arquitecta de Software")
    
    print("\n" + "=" * 60)
    
    # Crear segunda persona
    persona2 = Persona(
        nombre="Carlos López",
        año_nacimiento=2010,
        genero="Masculino",
        nacionalidad="Español",
        profesion="Estudiante",
        estado_civil="Soltero",
        altura=1.50,
        peso=45
    )
    
    print("\nPersona 2 creada:")
    # Usar __str__ (se llama automáticamente con print)
    print(persona2)
    
    persona2.agregar_hobby("Fútbol")
    persona2.agregar_hobby("Videojuegos")
    
    persona2.mostrar_info_completa()
    print(f"\n¿Es mayor de edad? {persona2.es_mayor_de_edad()}")
    
    print("\n" + "=" * 60)
    print("RESUMEN DE MÉTODOS IMPLEMENTADOS:")
    print("✓ saludar() - Método requerido")
    print("✓ calcular_edad() - Método adicional 1")
    print("✓ calcular_imc() - Método adicional 2") 
    print("✓ agregar_hobby() - Método adicional 3")
    print("✓ mostrar_info_completa() - Método adicional 4")
    print("✓ cambiar_profesion() - Método adicional 5")
    print("✓ es_mayor_de_edad() - Método adicional 6")
    print("✓ __str__() - Representación especial")