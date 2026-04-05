import streamlit as st

# CONFIG
st.set_page_config(page_title="Mis Finanzas", layout="centered")

# ESTILO (CSS)
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1, h2, h3 {
    color: #00C2FF;
}
.stButton>button {
    background-color: #00C2FF;
    color: black;
    font-weight: bold;
    border-radius: 8px;
}

/* TARJETAS */
.card {
    background-color: palegreen;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 10px;
}
.card-title {
    font-size: 14px;
    color: #555;
}
.card-value {
    font-size: 26px;
    font-weight: bold;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# 🔥 FUNCIÓN TARJETA (AGREGADO)
def card(titulo, valor):
    return f"""
    <div class="card">
        <div class="card-title">{titulo}</div>
        <div class="card-value">{valor}</div>
    </div>
    """

# HEADER
st.title("💰 Mis Finanzas")
st.caption("Analiza tu situación financiera en segundos")

# TABS (FLUJO PRO)
tab1, tab2, tab3 = st.tabs(["1️⃣ Datos", "2️⃣ Análisis", "3️⃣ Resultado"])

# -------------------------
# TAB 1: INPUTS
# -------------------------
with tab1:

    st.subheader("📥 Ingresa tus datos")

    ingreso = st.number_input("💰 Ingreso mensual", min_value=0.0, placeholder="Ej: 50000")

    modo_gastos = st.radio(
        "¿Cómo quieres ingresar tus gastos?",
        ["Gasto total", "Por categorías"]
    )

    if modo_gastos == "Gasto total":
        gastos = st.number_input("🧾 Gasto total mensual", min_value=0.0)

    else:
        st.markdown("### 📊 Desglose de gastos")

        col1, col2 = st.columns(2)

        with col1:
            alimentos = st.number_input("🍽️ Alimentos", min_value=0.0)
            vivienda = st.number_input("🏠 Vivienda", min_value=0.0)
            salud = st.number_input("🏥 Salud", min_value=0.0)
            transporte = st.number_input("🚗 Transporte", min_value=0.0)

        with col2:
            vestimenta = st.number_input("👕 Vestimenta", min_value=0.0)
            muebles = st.number_input("🛋️ Muebles", min_value=0.0)
            educacion = st.number_input("🎓 Educación", min_value=0.0)
            otros = st.number_input("📦 Otros", min_value=0.0)

        gastos = (
            alimentos + vivienda + salud + transporte +
            vestimenta + muebles + educacion + otros
        )

        st.success(f"💰 Total gastos: $ {gastos:,.0f}".replace(",", "."))

    deuda = st.number_input("💳 Pago mensual de deudas", min_value=0.0)

    # FEEDBACK INMEDIATO
    if ingreso > 0:
        disponible_preview = ingreso - gastos - deuda
        st.info(f"💡 Te quedarían aproximadamente $ {disponible_preview:,.0f}".replace(",", "."))


# -------------------------
# TAB 2: ANALISIS
# -------------------------
with tab2:

    st.subheader("📊 Análisis de tu situación")

    if ingreso > 0:

        endeudamiento = (deuda / ingreso) * 100 if ingreso > 0 else 0
        disponible = ingreso - gastos - deuda

        # 🔥 TARJETAS (AGREGADO)
        col1, col2, col3 = st.columns(3)
        col1.markdown(card("💰 Ingreso", f"$ {ingreso:,.0f}".replace(",", ".")), unsafe_allow_html=True)
        col2.markdown(card("🧾 Gastos", f"$ {gastos:,.0f}".replace(",", ".")), unsafe_allow_html=True)
        col3.markdown(card("💵 Disponible", f"$ {disponible:,.0f}".replace(",", ".")), unsafe_allow_html=True)

        # TU LÓGICA ORIGINAL (INTACTA)
        col1, col2 = st.columns(2)
        col1.metric("💵 Disponible", f"$ {disponible:,.0f}".replace(",", "."))
        col2.metric("📊 Endeudamiento", f"{endeudamiento:.1f}%")

        st.progress(min(max(endeudamiento / 100, 0), 1))

        if disponible < 0:
            st.error("🔴 Estás gastando más de lo que ganas")
        elif disponible < ingreso * 0.2:
            st.warning("🟡 Estás en una zona ajustada")
        else:
            st.success("🟢 Buena situación financiera")

    else:
        st.warning("Ingresa tus datos en la pestaña anterior")


# -------------------------
# TAB 3: RESULTADO
# -------------------------
with tab3:

    st.subheader("🎯 Resultado final")

    if ingreso > 0:

        disponible = ingreso - gastos - deuda
        endeudamiento = (deuda / ingreso) * 100

        # 🔥 TARJETAS (AGREGADO)
        col1, col2, col3 = st.columns(3)
        col1.markdown(card("💰 Ingreso", f"$ {ingreso:,.0f}".replace(",", ".")), unsafe_allow_html=True)
        col2.markdown(card("🧾 Gastos", f"$ {gastos:,.0f}".replace(",", ".")), unsafe_allow_html=True)
        col3.markdown(card("💵 Disponible", f"$ {disponible:,.0f}".replace(",", ".")), unsafe_allow_html=True)

        # TU LÓGICA ORIGINAL (INTACTA)
        if disponible < 0 or endeudamiento > 50:
            st.error("🔴 Riesgo ALTO")
            recomendaciones = [
                "Reduce gastos urgentemente",
                "Evita nuevas deudas",
                "Prioriza pagos importantes"
            ]

        elif disponible < ingreso * 0.2 or endeudamiento >= 30:
            st.warning("🟡 Riesgo MODERADO")
            recomendaciones = [
                "Ajusta pequeños gastos",
                "Evita endeudarte más",
                "Intenta aumentar ahorro"
            ]

        else:
            st.success("🟢 Situación SALUDABLE")
            recomendaciones = [
                "Puedes ahorrar o invertir",
                "Mantén el control de gastos",
                "Planifica a futuro"
            ]

        st.markdown("### 🚀 ¿Qué puedes hacer?")
        for r in recomendaciones:
            st.write(f"👉 {r}")

        st.markdown("### 📉 Impacto en 12 meses")

        impacto = disponible * 12

        if disponible < 0:
            st.error(f"Perderías $ {impacto:,.0f}".replace(",", "."))
        else:
            st.success(f"Podrías acumular $ {impacto:,.0f}".replace(",", "."))

    else:
        st.warning("Completa tus datos primero")
