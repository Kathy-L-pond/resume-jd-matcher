import streamlit as st
from resume_jd_matcher.crew import ResumeJdMatcher
import pypdf
import io

st.set_page_config(page_title="AI简历优化 & JD匹配Agent", layout="wide")
st.title("🚀 AI简历优化 & JD匹配Agent")
st.markdown("**上传简历PDF + 粘贴JD → 自动生成匹配分析 + 优化简历 + Cover Letter**")

# 左侧：输入区
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📄 上传你的简历 (PDF)")
    uploaded_file = st.file_uploader("选择PDF文件", type=["pdf"])
    
    st.subheader("📋 粘贴职位描述 (JD)")
    user_jd = st.text_area("JD内容", height=300, placeholder="把JD粘贴在这里...")

# PDF 提取函数
def extract_text_from_pdf(pdf_file):
    pdf_reader = pypdf.PdfReader(io.BytesIO(pdf_file.getvalue()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# 右侧：运行按钮和结果区
with col2:
    if st.button("🚀 一键生成匹配分析 + 优化简历 + Cover Letter", type="primary", use_container_width=True):
        if not uploaded_file:
            st.error("请先上传简历PDF")
        elif not user_jd.strip():
            st.error("请先粘贴JD")
        else:
            with st.spinner("AI Agent团队正在工作（5个Agent协作中）..."):
                # 提取简历文本
                user_resume = extract_text_from_pdf(uploaded_file)
                
                # 准备输入
                inputs = {
                    "user_jd": user_jd,
                    "user_resume": user_resume
                }
                
                # 运行CrewAI
                result = ResumeJdMatcher().crew().kickoff(inputs=inputs)
                
                # 显示结果
                st.success("✅ Agent团队完成任务！")
                st.markdown("### 📊 最终输出")
                st.markdown(result.raw)

# 底部说明
st.caption("技术栈：CrewAI（多Agent） + Streamlit（网页） + Groq（免费LLM）")
st.caption("这是你的第一个完整AI产品Demo，可直接部署到Streamlit Cloud")