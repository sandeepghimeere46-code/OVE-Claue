package com.oveclaue.app.ui

import android.Manifest
import android.content.Intent
import android.os.Bundle
import android.speech.RecognitionListener
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Mic
import androidx.compose.material.icons.filled.Send
import androidx.compose.material.icons.filled.Stop
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun VoiceInputBar(
    onSend: (String) -> Unit,
    onStopToText: (String) -> Unit,
    onCancel: () -> Unit
) {
    val context = LocalContext.current
    var recognizedText by remember { mutableStateOf("Listening...") }
    var isListening by remember { mutableStateOf(false) }

    val speechRecognizer = remember {
        SpeechRecognizer.createSpeechRecognizer(context).apply {
            setRecognitionListener(object : RecognitionListener {
                override fun onReadyForSpeech(params: Bundle?) {}
                override fun onBeginningOfSpeech() { recognizedText = "Listening..." }
                override fun onRmsChanged(rmsdB: Float) {}
                override fun onBufferReceived(buffer: ByteArray?) {}
                override fun onEndOfSpeech() {}
                override fun onError(error: Int) {
                    recognizedText = "Error listening. Tap cancel."
                    isListening = false
                }
                override fun onResults(results: Bundle?) {
                    val matches = results?.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)
                    if (!matches.isNullOrEmpty()) {
                        recognizedText = matches[0]
                    }
                    isListening = false
                }
                override fun onPartialResults(results: Bundle?) {
                    val matches = results?.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)
                    if (!matches.isNullOrEmpty()) {
                        recognizedText = matches[0]
                    }
                }
                override fun onEvent(eventType: Int, params: Bundle?) {}
            })
        }
    }

    val startListening = {
        val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
            putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            putExtra(RecognizerIntent.EXTRA_PARTIAL_RESULTS, true)
        }
        speechRecognizer.startListening(intent)
        isListening = true
        recognizedText = "Listening..."
    }

    val permissionLauncher = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted ->
        if (isGranted) {
            startListening()
        } else {
            onCancel()
        }
    }

    DisposableEffect(Unit) {
        permissionLauncher.launch(Manifest.permission.RECORD_AUDIO)
        onDispose {
            speechRecognizer.destroy()
        }
    }

    Surface(
        shape = RoundedCornerShape(26.dp),
        color = MaterialTheme.colorScheme.surfaceVariant,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 6.dp, vertical = 6.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            // Cancel Button
            IconButton(
                onClick = {
                    speechRecognizer.stopListening()
                    onCancel()
                },
                modifier = Modifier.size(40.dp),
            ) {
                Icon(
                    imageVector = Icons.Default.Close,
                    contentDescription = "Cancel voice recording",
                    tint = MaterialTheme.colorScheme.onSurfaceVariant
                )
            }

            // Live Text Display
            Text(
                text = recognizedText,
                modifier = Modifier.weight(1f).padding(horizontal = 8.dp),
                color = MaterialTheme.colorScheme.onSurface,
                fontSize = 15.sp,
                maxLines = 2,
                overflow = TextOverflow.Ellipsis
            )

            // Stop to Textbox
            IconButton(
                onClick = {
                    speechRecognizer.stopListening()
                    val textToReturn = if (recognizedText == "Listening..." || recognizedText.startsWith("Error")) "" else recognizedText
                    onStopToText(textToReturn)
                },
                modifier = Modifier.size(40.dp),
            ) {
                Icon(
                    imageVector = Icons.Default.Stop,
                    contentDescription = "Stop recording and edit text",
                    tint = MaterialTheme.colorScheme.primary
                )
            }

            Spacer(Modifier.width(4.dp))

            // Send Button
            Box(
                modifier = Modifier
                    .size(38.dp)
                    .background(
                        color = MaterialTheme.colorScheme.primary,
                        shape = CircleShape,
                    )
                    .clickable(
                        onClickLabel = "Send voice message directly",
                        onClick = {
                            speechRecognizer.stopListening()
                            val textToReturn = if (recognizedText == "Listening..." || recognizedText.startsWith("Error")) "" else recognizedText
                            if (textToReturn.isNotBlank()) {
                                onSend(textToReturn)
                            } else {
                                onCancel()
                            }
                        }
                    ),
                contentAlignment = Alignment.Center,
            ) {
                Icon(
                    imageVector = Icons.Default.Send,
                    contentDescription = "Send voice message directly",
                    tint = MaterialTheme.colorScheme.onPrimary,
                    modifier = Modifier.size(18.dp),
                )
            }
        }
    }
}
