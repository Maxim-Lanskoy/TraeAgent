# Copyright (c) 2025 ByteDance Ltd., Maxim Lanskoy and/or its affiliates
# SPDX-License-Identifier: MIT

"""LM Studio client wrapper for local LLM models"""

import openai

from trae_agent.utils.config import ModelConfig
from trae_agent.utils.llm_clients.openai_compatible_base import (
    OpenAICompatibleClient,
    ProviderConfig,
)


class LMStudioProvider(ProviderConfig):
    """LM Studio provider configuration."""

    def create_client(
        self, api_key: str, base_url: str | None, api_version: str | None
    ) -> openai.OpenAI:
        """Create OpenAI client with LM Studio base URL.
        
        LM Studio doesn't require an API key, but we need to provide something
        for the OpenAI client to work properly.
        """
        # Use a dummy API key if none is provided
        api_key = api_key or "lm-studio"
        # Use the provided base URL or default to localhost
        base_url = base_url or "http://localhost:1234/v1"
        
        return openai.OpenAI(
            base_url=base_url,
            api_key=api_key,
        )

    def get_service_name(self) -> str:
        """Get the service name for retry logging."""
        return "LMStudio"

    def get_provider_name(self) -> str:
        """Get the provider name for trajectory recording."""
        return "lm-studio"

    def get_extra_headers(self) -> dict[str, str]:
        """Get LM Studio-specific headers (none needed)."""
        return {}

    def supports_tool_calling(self, model_name: str) -> bool:
        """Check if the model supports tool calling.
        
        Most LM Studio models support function/tool calling,
        but this depends on the specific model being used.
        """
        # You can add specific model checks here if needed
        # For now, we'll assume tool calling is supported
        return True


class LMStudioClient(OpenAICompatibleClient):
    """LM Studio client wrapper for local LLM models."""

    def __init__(self, model_config: ModelConfig):
        # Set default base URL if not provided
        if not model_config.model_provider.base_url:
            model_config.model_provider.base_url = "http://localhost:1234/v1"
        
        # Set default API key if not provided (LM Studio doesn't require authentication)
        if not model_config.model_provider.api_key:
            model_config.model_provider.api_key = "lm-studio"
        
        super().__init__(model_config, LMStudioProvider())
