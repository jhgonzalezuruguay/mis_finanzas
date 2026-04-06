import streamlit as st

# CONFIG
st.set_page_config(page_title="Mis Finanzas", layout="centered")

# ESTILO (CSS)
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}1, h2, h3 {
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
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.card {
    animation: fadeIn 0.6s ease-in-out;
}
.card:hover {
    transform: scale(1.3);
    transition: 0.2s;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
/* HOVER TARJETA DE RIESGO */
.risk-card:hover {
    transform: scale(1.3);
    transition: all 0.2s ease-in-out;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
}

.impact-card:hover {
    transform: translateY(-5px) scale(1.2);
    transition: all 0.25s ease;
    box-shadow: 0px 12px 25px rgba(0,0,0,0.4);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.3); }
    100% { transform: scale(1); }
}

/* 👇 ACÁ ESTÁ LA CLAVE */
.risk-card {
    animation: fadeIn 0.6s ease-in-out, pulse 2s infinite;
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
def risk_card(titulo, mensaje, color):
    return f"""
    <div class="risk-card" style="
        background:lightgrey;
        padding:20px;
        border-radius:12px;
        margin-top:10px;
        border-left:8px solid {color};
    ">
        <h3 style="margin:0; color:{color};">{titulo}</h3>
        <p style="margin-top:10px; color:#333;">{mensaje}</p>
    </div>
    """

def impacto_card(titulo, valor, color):
    return f"""
    <div class="impact-card" style="
        background:lightgrey;
        padding:20px;
        border-radius:12px;
        margin-top:10px;
        border-left:8px solid {color};
        animation: fadeIn 0.6s ease-in-out;
        text-align:center;
    ">
        <h3 style="margin:0; color:{color};">{titulo}</h3>
        <h1 style="margin-top:10px; color:#000;">{valor}</h1>
    </div>
    """
# HEADER
st.title("💰 MIS FINANZAS")
st.caption("Analiza tu situación financiera en segundos")

# TABS (FLUJO PRO)
tab1, tab2, tab3 = st.tabs(["1️⃣ DATOS", "2️⃣ ANÁLISIS", "3️⃣ RESULTADO"])

# -------------------------
# TAB 1: INPUTS
# -------------------------
with tab1:

    st.subheader("📥 INGRESA TUS DATOS")

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
            vivienda = st.number_input("🏠 Vivienda y suministros", min_value=0.0)
            salud = st.number_input("🏥 Salud", min_value=0.0)
            transporte = st.number_input("🚗 Transporte y comunicaciones", min_value=0.0)

        with col2:
            vestimenta = st.number_input("👕 Vestimenta y calzado", min_value=0.0)
            muebles = st.number_input("🛋️ Muebles y electrodomésticos", min_value=0.0)
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
        st.info(f"💡 Te quedan aproximadamente $ {disponible_preview:,.0f}".replace(",", "."))


# -------------------------
# TAB 2: ANALISIS
# -------------------------
with tab2:

    st.subheader("📊 ANÁLISIS DE TU SITUACIÓN")

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

        progress = min(max(endeudamiento / 100, 0), 1)
        bar = st.progress(0)

        for i in range(int(progress * 100)):
            bar.progress(i + 1)

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

    st.subheader("🎯 RESULTADO FINAL")

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
            st.markdown(
                risk_card(
                "🔴 RIESGO ALTO",
                "Estás en zona de peligro financiero. Necesitas reducir gastos o deudas urgentemente.",
                "#FF5252"
                ),
                unsafe_allow_html=True
            )

            recomendaciones = [
                "Reduce gastos urgentemente",
                "Evita nuevas deudas",
                "Prioriza pagos importantes"
            ]

        elif disponible < ingreso * 0.2 or endeudamiento >= 30:
            st.markdown(
                risk_card(
                    "🟡 RIESGO MODERADO",
                    "Estás en una zona de alerta. Conviene ajustar tus finanzas.",
                    "orange"
                ),
                unsafe_allow_html=True
            )

            recomendaciones = [
                "Ajusta pequeños gastos",
                "Evita endeudarte más",
                "Intenta aumentar ahorro"
            ]

        else:
            st.markdown(
                risk_card(
                    "🟢 SIN RIESGO",
                    "Tu situación es saludable. Puedes planificar ahorro o inversión.",
                    "darkgreen"
                ),
                unsafe_allow_html=True
            )

            recomendaciones = [
                "Puedes ahorrar o invertir",
                "Mantén el control de gastos",
                "Planifica a futuro"
            ]

        st.markdown("### 🚀 ¿Qué puedes hacer?")
        for r in recomendaciones:
            st.write(f"👉 {r}")

        st.markdown("### 📉 IMPACTO EN 12 MESES")

        impacto = disponible * 12
        impacto_fmt = f"$ {impacto:,.0f}".replace(",", ".")

        if disponible < 0:
            st.markdown(
                impacto_card(
                    "🔴 Impacto negativo",
                    f"Perderías {impacto_fmt} en 1 año",
                    "#FF5252"
                ),
                unsafe_allow_html=True
            )

        elif disponible == 0:
            st.markdown(
                impacto_card(
                    "🟡 Sin impacto",
                    "No generarías ahorro ni pérdida en 1 año",
                    "orange"
                ),
                unsafe_allow_html=True
            )

        else:
            st.markdown(
                impacto_card(
                    "🟢 Impacto positivo",
                    f"Podrías acumular {impacto_fmt} en 1 año",
                    "#00C853"
                ),
                unsafe_allow_html=True
            )
