import streamlit as st
import streamlit.components.v1 as components

st.title("Gomoku Game")

# 오목 게임 코드
html_code = """
<div style="display: flex; flex-direction: column; align-items: center;">
    <h3 id="status">Black Turn</h3>
    <canvas id="board" width="400" height="400" style="background: #ffce9e; border: 2px solid #333;"></canvas>
    <script>
        const canvas = document.getElementById('board');
        const ctx = canvas.getContext('2d');
        const size = 15;
        const cellSize = 25;
        const padding = 25;

        function draw() {
            ctx.strokeStyle = '#000';
            for (let i = 0; i < size; i++) {
                ctx.beginPath();
                ctx.moveTo(padding, padding + i * cellSize);
                ctx.lineTo(padding + (size-1)*cellSize, padding + i * cellSize);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(padding + i * cellSize, padding);
                ctx.lineTo(padding + i * cellSize, padding + (size-1)*cellSize);
                ctx.stroke();
            }
        }
        draw();
    </script>
</div>
"""
components.html(html_code, height=500)
