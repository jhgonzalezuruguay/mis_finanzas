import streamlit as st

# 1. Configuración
st.set_page_config(
    page_title="Mis Finanzas",
    layout="centered"
)

# 2. Título
st.title("💰 Mis Finanzas")
st.write("Descubre tu nivel de riesgo financiero en segundos")

# 3. Inputs
ingreso = st.number_input("💰 Ingreso mensual", min_value=0.0)
gastos = st.number_input("🧾 Gastos mensuales", min_value=0.0)
deuda = st.number_input("💳 Pago mensual de deudas", min_value=0.0)
# Vista formateada (opcional pero profesional)
if ingreso > 0:
    ingreso_fmt = f"$ {ingreso:,.0f}".replace(",", ".")
    gastos_fmt = f"$ {gastos:,.0f}".replace(",", ".")
    deuda_fmt = f"$ {deuda:,.0f}".replace(",", ".")

    st.write("### 📊 Resumen ingresado")
    st.write(f"Ingreso: {ingreso_fmt}")
    st.write(f"Gastos: {gastos_fmt}")
    st.write(f"Deuda: {deuda_fmt}")
# 4. Botón
calcular = st.button("Calcular mi situación")

# 5. Lógica
if calcular:

    if ingreso == 0:
        st.warning("Por favor ingresa un ingreso mayor a 0")
    
    else:
        # Cálculos
        disponible = ingreso - gastos - deuda
        endeudamiento = (deuda / ingreso) * 100

        # Clasificación
        if disponible < 0 or endeudamiento > 50:
            riesgo = "🔴 Riesgo financiero ALTO"
        
        elif (disponible >= 0 and disponible < ingreso * 0.2) or (30 <= endeudamiento <= 50):
            riesgo = "🟡 Riesgo MODERADO"
        
        else:
            riesgo = "🟢 Situación SALUDABLE"

        # 6. Resultado visual (WOW)
        st.write("---")

        if "ALTO" in riesgo:
            st.error(riesgo)
            st.write("⚠️ Estás gastando más de lo que puedes sostener.")
            st.write("👉 Recomendación: reduce gastos o deudas urgentemente.")

        elif "MODERADO" in riesgo:
            st.warning(riesgo)
            st.write("⚠️ Estás en una zona de riesgo.")
            st.write("👉 Recomendación: intenta aumentar tu ahorro.")

        else:
            st.success(riesgo)
            st.write("✅ Vas por buen camino.")
            st.write("👉 Podrías ahorrar o invertir ese excedente.")

        # 7. Detalle
        st.write("---")
        
        
        # Formato dinero
        dinero_formateado = f"$ {disponible:,.0f}".replace(",", ".")

        # Resultado
        st.write(f"💵 Dinero disponible: {dinero_formateado}")
        st.write(f"📊 Endeudamiento: {endeudamiento:.1f}%")
