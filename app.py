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
ingreso = st.number_input("💰 INGRESO MENSUAL", min_value=0.0)

modo_gastos = st.radio(
    "¿Cómo quieres ingresar tus gastos?",
    ["Gasto Total Mensual", "Por categorías"]
)

if modo_gastos == "Gasto Total Mensual":
    gastos = st.number_input("🧾 Gasto total mensual", min_value=0.0)

else:
    st.write("### 📊 Desglose de gastos mensuales")

    alimentos = st.number_input("Alimentos y bebidas", min_value=0.0)
    vestimenta = st.number_input("Vestimenta y calzado", min_value=0.0)
    vivienda = st.number_input("Vivienda", min_value=0.0)
    muebles = st.number_input("Muebles y accesorios", min_value=0.0)
    salud = st.number_input("Cuidados médicos", min_value=0.0)
    transporte = st.number_input("Transporte y comunicaciones", min_value=0.0)
    esparcimiento = st.number_input("Esparcimiento", min_value=0.0)
    educacion = st.number_input("Enseñanza/educación", min_value=0.0)
    otros = st.number_input("Otros gastos", min_value=0.0)

    gastos = (
        alimentos + vestimenta + vivienda + muebles +
        salud + transporte + esparcimiento + educacion + otros
    )

    # Mostrar total
    gastos_fmt = f"$ {gastos:,.0f}".replace(",", ".")
    st.success(f"💰 Total de gastos: {gastos_fmt}")

    # 🔥 Análisis INE (AHORA BIEN UBICADO)
    st.write("### 📊 Análisis de gastos (comparado con promedio INE)")

    if ingreso > 0:

        porc_alimentos = (alimentos / ingreso) * 100
        porc_vestimenta = (vestimenta / ingreso) * 100
        porc_vivienda = (vivienda / ingreso) * 100
        porc_muebles = (muebles / ingreso) * 100
        porc_salud = (salud / ingreso) * 100
        porc_transporte = (transporte / ingreso) * 100
        porc_esparcimiento = (esparcimiento / ingreso) * 100
        porc_educacion = (educacion / ingreso) * 100
        porc_otros = (otros / ingreso) * 100

        ref = {
            "Alimentos": 28.47,
            "Vestimenta": 6.84,
            "Vivienda": 13.20,
            "Muebles": 7.16,
            "Salud": 14.26,
            "Transporte": 14.26,
            "Esparcimiento": 5.78,
            "Educación": 4.28,
            "Otros": 5.75
        }

        def evaluar(nombre, valor, referencia):
            if valor > referencia * 1.3:
                st.warning(f"⚠️ {nombre}: muy por encima del promedio ({valor:.1f}% vs {referencia}%)")
            elif valor > referencia:
                st.info(f"ℹ️ {nombre}: levemente por encima del promedio ({valor:.1f}% vs {referencia}%)")

        evaluar("Alimentos", porc_alimentos, ref["Alimentos"])
        evaluar("Vestimenta", porc_vestimenta, ref["Vestimenta"])
        evaluar("Vivienda", porc_vivienda, ref["Vivienda"])
        evaluar("Muebles", porc_muebles, ref["Muebles"])
        evaluar("Salud", porc_salud, ref["Salud"])
        evaluar("Transporte", porc_transporte, ref["Transporte"])
        evaluar("Esparcimiento", porc_esparcimiento, ref["Esparcimiento"])
        evaluar("Educación", porc_educacion, ref["Educación"])
        evaluar("Otros", porc_otros, ref["Otros"])

        # 🔥 Presupuesto ideal según INE
        st.write("---")
        st.subheader("💡 Presupuesto recomendado (según tu ingreso)")

        if ingreso > 0:

            presupuesto = {
                "Alimentos": ingreso * 0.2847,
                "Vestimenta": ingreso * 0.0684,
                "Vivienda": ingreso * 0.1320,
                "Muebles": ingreso * 0.0716,
                "Salud": ingreso * 0.1426,
                "Transporte": ingreso * 0.1426,
                "Esparcimiento": ingreso * 0.0578,
                "Educación": ingreso * 0.0428,
                "Otros": ingreso * 0.0575
            }

            for rubro, valor in presupuesto.items():
                valor_fmt = f"$ {valor:,.0f}".replace(",", ".")
                st.write(f"{rubro}: {valor_fmt}")


        

# Input deuda (fuera del if, correcto)
deuda = st.number_input("💳 Pago mensual de deudas", min_value=0.0)

# Vista formateada
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
            riesgo = "🔴 Riesgo ALTO!!. Estás en zona de peligro financiero!"
        
        elif (disponible >= 0 and disponible < ingreso * 0.2) or (30 <= endeudamiento <= 50):
            riesgo = "🟡 Riesgo MODERADO. Estás en zona de alerta. Realiza ajustes..."
        
        else:
            riesgo = "🟢 Estás en situación y zona SALUDABLE. Felicitaciones!"

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
        # Mensaje más humano
        st.write("---")

        if disponible < 0:
            st.write("💬 Estás viviendo por encima de tus posibilidades.")
        elif disponible < ingreso * 0.2:
            st.write("💬 Estás muy justo, cualquier imprevisto puede complicarte.")
        else:
            st.write("💬 Tienes margen, estás haciendo las cosas bien.")
        # 8. Recomendaciones personalizadas
        st.write("---")
        st.subheader("📌 ¿Qué puedes hacer?")

        if disponible < 0:
            deficit = abs(disponible)
            st.write(f"🔴 Te faltan aproximadamente $ {deficit:,.0f}".replace(",", "."))
            st.write("👉 Reduce gastos o aumenta ingresos urgentemente.")
            st.write("👉 Prioriza pagar deudas con intereses altos.")

        elif disponible < ingreso * 0.2:
            necesario = ingreso * 0.2 - disponible
            st.write(f"🟡 Te faltan $ {necesario:,.0f} para estar en zona segura.".replace(",", "."))
            st.write("👉 Intenta reducir gastos pequeños.")
            st.write("👉 Evita nuevas deudas.")

        else:
            ahorro = disponible
            st.write(f"🟢 Podrías ahorrar aproximadamente $ {ahorro:,.0f}".replace(",", "."))
            st.write("👉 Considera ahorrar o invertir ese dinero.")
            st.write("👉 Mantén tus gastos bajo control.")

        # Recomendación adicional por endeudamiento
        if endeudamiento > 50:
            st.write("⚠️ Tu nivel de deuda es muy alto respecto a tu ingreso.")
        elif endeudamiento > 30:
            st.write("⚠️ Tu nivel de deuda empieza a ser riesgoso.")

        # 9. Impacto mensual acumulado
        st.write("---")
        st.subheader("📉 Impacto en el tiempo")

        impacto_anual = disponible * 12

        impacto_fmt = f"$ {impacto_anual:,.0f}".replace(",", ".")

        if disponible < 0:
            st.write(f"🔴 En 1 año acumularías una deuda de aproximadamente {impacto_fmt}")
        elif disponible < ingreso * 0.2:
            st.write(f"🟡 En 1 año ahorrarías solo {impacto_fmt}")
        else:
            st.write(f"🟢 En 1 año podrías ahorrar {impacto_fmt}")
