package com.oveclaue.app.ui

import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.input.OffsetMapping
import androidx.compose.ui.text.input.TransformedText
import androidx.compose.ui.text.input.VisualTransformation
import java.util.regex.Pattern

class SyntaxHighlighter : VisualTransformation {
    override fun filter(text: AnnotatedString): TransformedText {
        val annotated = buildAnnotatedString {
            append(text.text)
            
            // Keywords
            val keywordPattern = Pattern.compile("\\b(val|var|fun|class|interface|if|else|when|for|while|return|true|false|null|import|package|const|suspend|let|const|function|=>|await|async|def|import|from|class)\\b")
            val keywordMatcher = keywordPattern.matcher(text.text)
            while (keywordMatcher.find()) {
                addStyle(SpanStyle(color = Color(0xFFFF7B72)), keywordMatcher.start(), keywordMatcher.end())
            }

            // Strings
            val stringPattern = Pattern.compile("\"[^\"]*\"|'[^']*'")
            val stringMatcher = stringPattern.matcher(text.text)
            while (stringMatcher.find()) {
                addStyle(SpanStyle(color = Color(0xFFA5D6FF)), stringMatcher.start(), stringMatcher.end())
            }

            // Comments
            val commentPattern = Pattern.compile("//.*|/\\*[\\s\\S]*?\\*/|#.*")
            val commentMatcher = commentPattern.matcher(text.text)
            while (commentMatcher.find()) {
                addStyle(SpanStyle(color = Color(0xFF8B949E)), commentMatcher.start(), commentMatcher.end())
            }
            
            // Numbers
            val numberPattern = Pattern.compile("\\b\\d+\\.?\\d*\\b")
            val numberMatcher = numberPattern.matcher(text.text)
            while (numberMatcher.find()) {
                addStyle(SpanStyle(color = Color(0xFF79C0FF)), numberMatcher.start(), numberMatcher.end())
            }
        }
        return TransformedText(annotated, OffsetMapping.Identity)
    }
}
