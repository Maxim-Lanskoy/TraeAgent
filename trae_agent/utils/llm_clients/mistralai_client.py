# Copyright (c) 2025 ByteDance Ltd., Maxim Lanskoy and/or its affiliates
# SPDX-License-Identifier: MIT

"""Mistral AI client wrapper for Mistral models"""

import openai

from trae_agent.utils.config import ModelConfig
from trae_agent.utils.llm_clients.openai_compatible_base import (
    OpenAICompatibleClient,
    ProviderConfig,
)

class MistralAIProvider(ProviderConfig):
    """Mistral AI provider configuration."""

    def create_client(
        self, api_key: str, base_url: str | None, api_version: str | None
    ) -> openai.OpenAI:
        """Create client with Mistral AI as a base URL.
        """
        # Use a dummy API key if none is provided
        api_key = api_key or "mistralai"
        # Use the provided base URL or default to Mistral API
        base_url = base_url or "https://api.mistral.ai/v1"
        
        return openai.OpenAI(
            base_url=base_url,
            api_key=api_key,
        )

    def get_service_name(self) -> str:
        """Get the service name for retry logging."""
        return "MistralAI"

    def get_provider_name(self) -> str:
        """Get the provider name for trajectory recording."""
        return "mistralai"

    def get_extra_headers(self) -> dict[str, str]:
        """Get Mistral AI-specific headers (none needed)."""
        return {}

    def supports_tool_calling(self, model_name: str) -> bool:
        """Check if the model supports tool calling.
        
        Mistral models support function/tool calling.
        """
        # Most Mistral models support tool calling
        # including mistral-large, mistral-medium, mistral-small
        return True


class MistralAIClient(OpenAICompatibleClient):
    """Mistral AI client wrapper for Mistral models."""

    def __init__(self, model_config: ModelConfig):
        # Set default base URL if not provided
        if not model_config.model_provider.base_url:
            model_config.model_provider.base_url = "https://api.mistral.ai/v1"
        
        # Set default API key if not provided (Mistral AI requires authentication)
        if not model_config.model_provider.api_key:
            model_config.model_provider.api_key = "mistralai"
        
        super().__init__(model_config, MistralAIProvider())

    def chat(
        self,
        messages,
        model_config,
        tools=None,
        reuse_history=True,
    ):
        """Handle message ordering for Mistral AI's strict requirements."""
        # If we're reusing history and the new messages start with a system message,
        # and our history ends with an assistant message, clear history to avoid ordering error
        if reuse_history and self.message_history and messages:
            parsed_new = self.parse_messages(messages)
            if (parsed_new and 
                parsed_new[0].get("role") == "system" and 
                self.message_history and 
                self.message_history[-1].get("role") == "assistant"):
                # Clear history to start fresh with new system message
                self.message_history = []
        
        return super().chat(messages, model_config, tools, reuse_history)
